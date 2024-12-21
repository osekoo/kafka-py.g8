# Kafka Project Template

This template outlines the process of setting up, building, and running a Kafka-based project using Giter8 templates and Docker. It includes producer and consumer examples written in Python for interacting with Kafka.



## Prerequisites
Ensure the following tools are installed on your system:

1. **Python 3.x**
   - [Install Python on Windows](https://www.python.org/downloads/windows/)
   - [Install Python on macOS](https://www.python.org/downloads/mac-os/)
   - [Install Python on Linux](https://www.python.org/downloads/source/)

   **Linux Users:** You can also install Python using your package manager:
   - Ubuntu/Debian: `sudo apt update && sudo apt install python3`
   - Fedora/Red Hat: `sudo dnf install python3`
   - Arch: `sudo pacman -S python`

2. **Docker**
   - [Install Docker on Windows](https://docs.docker.com/desktop/install/windows-install/)
   - [Install Docker on macOS](https://docs.docker.com/desktop/install/mac-install/)
   - [Install Docker on Linux](https://docs.docker.com/desktop/install/linux-install/)

   **Linux Users:** Alternatively, install Docker using your package manager:
   - Ubuntu/Debian: `sudo apt update && sudo apt install docker.io`
   - Fedora/Red Hat: `sudo dnf install docker`
   - Arch: `sudo pacman -S docker`

3. **Docker Compose**
   - Docker Compose is included by default with Docker Desktop on Windows and macOS.
   - For Linux:
     - Follow the official guide to [install Docker Compose on Linux](https://docs.docker.com/compose/install/linux/).
     - Alternatively, you can install it manually:
       ```bash
       sudo curl -L "https://github.com/docker/compose/releases/download/2.x.x/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
       sudo chmod +x /usr/local/bin/docker-compose
       ```



## Setting up Kafka

- **Start Kafka Broker:**  
  From a terminal run the following command:
  ```bash
  kafka-start
  ```
  
- **Kafka Dashboard**  
  From web browser:
  ```
  http://localhost:9094
  ```
  
- **Stop Kafka Broker:**  
  From a terminal run the following command:
  ```bash
  kafka-stop
  ```

## Install requirements
```bash
python -m pip install -r requirements.txt
```

## Example: Kafka Producer (`producer.py`)
This example sends a series of numbers as messages to a Kafka topic.

### Code:
```python
import json
import time
from kafka import KafkaProducer

# Configuration
TOPIC_NAME = 'example_topic'
BROKER = 'localhost:9092'

def data_serializer(data):
    """
    Converts the given data into JSON format.
    :param data: Data to convert into JSON.
    :return: JSON data.
    """
    return json.dumps(data).encode('utf-8')

def send(producer, size):
    """
    Sends messages to the Kafka topic.
    :param producer: KafkaProducer instance.
    :param size: Number of messages to send.
    """
    for i in range(size):
        message = {'message': i}
        print(f'Sending: {message}')
        producer.send(TOPIC_NAME, value=message)
        time.sleep(1)  # Pause between messages

    producer.flush()

if __name__ == "__main__":
    producer = KafkaProducer(
        bootstrap_servers=BROKER,
        value_serializer=data_serializer
    )
    send(producer, size=10)
```

### Run:
```bash
python producer.py
```



## Example: Kafka Consumer (`consumer.py`)
This example reads messages from a Kafka topic.

### Code:
```python
import json
from kafka import KafkaConsumer

# Configuration
TOPIC_NAME = 'example_topic'
BROKER = 'localhost:9092'

def data_deserializer(data):
    """
    Converts JSON bytes to Python dictionary.
    :param data: JSON bytes data.
    :return: Python dictionary.
    """
    return json.loads(data.decode('utf-8'))

def receive(consumer):
    """
    Reads messages from the Kafka topic.
    :param consumer: KafkaConsumer instance.
    """
    for message in consumer:
        print(f"Read: {message.value['message']}")

if __name__ == "__main__":
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=BROKER,
        value_deserializer=data_deserializer,
        auto_offset_reset='earliest',
        enable_auto_commit=True
    )
    receive(consumer)
```

### Run:
```bash
python consumer.py
```



This template provides the foundational setup for creating a Kafka project using Docker and Giter8 templates. Extend it to fit more complex requirements, such as integrating with a database, implementing advanced message serialization, or scaling to multiple brokers.
