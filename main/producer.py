import pika, json

params = pika.URLParameters('amqps://yxggoesr:QUZTwDAVAuU_92tJ4vLyM3MVyG8_MMhh@jackal.rmq.cloudamqp.com/yxggoesr')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)