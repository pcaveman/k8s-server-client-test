import socket
import time
import logging 

class Client:
    #def __init__(self, host='localhost', port=8182):
    #def __init__(self, host='10.152.183.83', port=8181):
    def __init__(self, host='server-service', port=8181):
        self.host = host
        self.port = port
        hname = socket.gethostname()
        logging.basicConfig(
            filename=f'/var/log/client/client_{hname}_log.log',  # Spécifiez le nom du fichier de log
            level=logging.DEBUG,  # Niveau de log minimal à capturer
            format='%(asctime)s - %(levelname)s - %(message)s'  # Format des messages de log
        )  
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, self.port))
            return True
        except OSError:
            logging.debug("connect() failed")
            return False

    def disconnect(self):
        self.client_socket.close()

    def status(self):
        try:
            self.client_socket.send(b'')
        except OSError:
            logging.debug("status() failed")
            return False
        return True

    def get_time(self):
        try:
            self.client_socket.sendall('GET TIME'.encode())
            return self.client_socket.recv(1024).decode()
        except OSError:
            logging.debug("get_time() failed")
            return "ERROR"

if __name__ == '__main__':
    client = Client()
      
    while True:
        while not client.status():
            client.connect()
            logging.info("Connected to the server.")
        print("Server time is:", client.get_time())
        time.sleep(10)
        
    client.disconnect()

