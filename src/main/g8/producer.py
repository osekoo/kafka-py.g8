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
