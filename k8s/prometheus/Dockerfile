# Dockerfile
FROM prom/prometheus

# Kopiere die prometheus.yml Konfigurationsdatei in das Image
COPY prometheus.yml /etc/prometheus/

# Exponiere den Prometheus-Port
EXPOSE 9090

# Startet den Prometheus-Server
CMD ["--config.file=/etc/prometheus/prometheus.yml"]