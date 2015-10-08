"""
Usage: k-recv.py <hostname>

"""

from kafka import KafkaConsumer
import logging
import sys

logging.basicConfig()

topic = b'my-topic'
if len(sys.argv) > 2:
    topic = sys.argv[2]

consumer = KafkaConsumer(topic,
                         group_id='my_group',
                         bootstrap_servers=[sys.argv[1] + ':9092'])

for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))

print("done.")

## end.
