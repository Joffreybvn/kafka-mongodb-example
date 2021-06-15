
# Kafka MongoDB Example

A simple example of interaction between a Kafka Producer, a Topic, a Consumer and a MongoDB database in Python.

## Quickstart

`docker-compose up -d`

- Kafdrop: http://localhost:9000/
- Mongo Express: http://localhost:8081/ 

#### Run the Consumer and Producer:

- `python consumer.py`
- `python producer.py`

## Other useful commands

#### Shell into a Kafka Docker:

`docker exec -it kafka-kafdrop_kafka_1 sh -c "cd /opt/kafka/bin && /bin/bash"`

#### Create a Kafka Topic:
Optionnal - The topic will be created when the producer send a message, or when the consumer try to retrieve message from the topic.

`./kafka-topics.sh --create --topic sample --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`

## Sources

Simple examples: 
- https://kafka-python.readthedocs.io/en/master/usage.html
- https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1

Warning about `python-kafka` library:

https://blog.datasyndrome.com/a-tale-of-two-kafka-clients-c613efab49df
