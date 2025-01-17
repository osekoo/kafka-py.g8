@echo off
echo "Starting Kafka broker..."
docker rm -f kafka-broker
docker run -it --rm --name kafka-broker --user root -p 9000:9000 -p 9092:9092 -p 9093:9093 ghcr.io/osekoo/kafka:3.5
