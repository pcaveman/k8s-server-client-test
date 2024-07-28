import socket
from datetime import datetime
import threading
import logging
import re

from prometheus_client import start_http_server, Counter

class Server:
    def __init__(self, host='0.0.0.0', port=8181):
        start_http_server(8000)
        self.host = host
        self.port = port
        self.clientsNumber = 0
        hname = socket.gethostname()
        metricname = re.sub(r'[^a-zA-Z0-9]', '_', hname)
        self.clientCounter = Counter(f'{metricname}_client_metric', 'Number of current connected clients')
        logging.basicConfig(
            filename=f'/var/log/server/{hname}_log.log',  # Spécifiez le nom du fichier de log
            level=logging.DEBUG,  # Niveau de log minimal à capturer
            format='%(asctime)s - %(levelname)s - %(message)s'  # Format des messages de log
        )   

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()


    def handle_client(self, client_socket):
        counted = False
        while True:
            request = client_socket.recv(1024).decode()
            if not request:
                break  # Si la requête est vide, nous quittons la boucle
            if request == 'GET TIME':
                if (counted == False):
                    counted = True
                    self.clientsNumber += 1
                    self.clientCounter.inc()
                hname = socket.gethostname()
                my_date = datetime.now().strftime(': %Y-%m-%d %H:%M:%S')
                current_time = f'{hname} : {my_date}' 
                client_socket.sendall(current_time.encode())
                logging.debug(f'current client numbers {self.clientsNumber}')
        client_socket.close()
        if (counted == True):
            self.clientsNumber -= 1
            self.clientCounter.dec()

    def run(self):
        logging.info(f'Starting server on {self.host}:{self.port}')
        while True:
            client_socket, _ = self.server_socket.accept()
            logging.info(f'Starting client connection')
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def status(self):
        return self.server_socket.fileno() != -1

if __name__ == '__main__':
    server = Server()
    try:
        server.run()
    except KeyboardInterrupt:
        print("Server is shutting down.")
