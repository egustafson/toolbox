"""
Usage k-swarm.py <hostname>

"""

from kafka import SimpleProducer, KafkaClient
import logging
import sys

logging.basicConfig()

kafka = KafkaClient(sys.argv[1] + ':9092')
kafka.ensure_topic_exists(b'my-topic')

producer = SimpleProducer(kafka)
for ii in range(100000):
    msg = "msg-{}".format(ii)
    producer.send_messages(b'my-topic', msg)

print("done.")

## end
