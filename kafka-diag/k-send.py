"""
Usage:  k-send.py <hostname>

"""

from kafka import SimpleProducer, KafkaClient
import logging
import sys

logging.basicConfig()

kafka = KafkaClient(sys.argv[1] + ':9092')
kafka.ensure_topic_exists(b'my-topic')

producer = SimpleProducer(kafka)
producer.send_messages(b'my-topic', b'some message')
producer.send_messages(b'my-topic', b'this method', b'is veriadic')

print("done.")

## end
