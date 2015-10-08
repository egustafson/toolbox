"""
Usage:  k-topic.py <host> [new-topic]

"""

from kafka import SimpleProducer, KafkaClient

import logging
import sys

logging.basicConfig()

kafka = KafkaClient(sys.argv[1] + ':9092')

if len(sys.argv) > 2:
    topic = sys.argv[2]
    print("creating topic: {0}".format(topic))
    kafka.ensure_topic_exists(topic)

for t in kafka.topics:
    print("{0!r}:".format(t))


#    print("  partitions: {0!r}:".format(kafka.get_partition_ids_for_topic(t)))
    
print("done.")

## end
