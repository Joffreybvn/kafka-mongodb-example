
from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

# Create a Kafka Consumer
consumer = KafkaConsumer(
    'numbers',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    auto_commit_interval_ms=1000,
    group_id='counters',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

# Connect to MongoDB
client = MongoClient(
    'localhost', 27017,
    username='root',
    password='example',
    authSource='admin',
    authMechanism='SCRAM-SHA-256'
)
collection = client.numbers.numbers

# Main loop - Triggered upon message receiving
for message in consumer:
    content = message.value
    print(content)

    # Add to the database
    collection.insert_one(content)
    print(f'{message} added to {collection}')
