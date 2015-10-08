"""
Usage:  k-send.py <hostname>

"""

from kafka import SimpleProducer, KafkaClient
import logging
import sys

logging.basicConfig()

topic = b'my-topic'
if len(sys.argv) > 2:
    topic = sys.argv[2]

kafka = KafkaClient(sys.argv[1] + ':9092')
#kafka.ensure_topic_exists(topic)

producer = SimpleProducer(kafka)
producer.send_messages(topic, b'some message')
producer.send_messages(topic, b'this method', b'is veriadic')

print("done.")

## end
