
from time import sleep
from json import dumps
from kafka import KafkaProducer

# Create a Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

# Send numbers from 0 to 999
for number in range(100):
    producer.send('numbers', value={'number': number})
    sleep(0.025)

# producer.flush()
