import pika

params = pika.URLParameters('amqps://hbflrvwb:ZehQAU5uAbv2DDKd5LoSdpKOkSWLPfiL@jellyfish.rmq.cloudamqp.com/hbflrvwb')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')