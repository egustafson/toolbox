"""
Usage:  k-debug.py <host>

"""

from kafka import SimpleProducer, KafkaClient
import logging

logging.basicConfig()

kafka = KafkaClient(sys.argv[1] + ':9092')
#producer = SimpleProducer(kafka)

#kafka.ensure_topic_exists(b'my-topic')

print("Client:  {0!r}".format(kafka))
md = kafka.send_metadata_request()
print("  {0!r}".format(md))

for t in kafka.topics:
    print("{0!r}:".format(t))
    print("  partitions: {0!r}:".format(kafka.get_partition_ids_for_topic(t)))
    
#kafka.ensure_topic_exists(b'my-topic')


print("done.")

## end
