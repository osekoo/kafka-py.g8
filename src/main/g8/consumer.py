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
