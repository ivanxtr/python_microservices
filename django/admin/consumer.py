import pika

params = pika.URLParameters('amqps://hbflrvwb:ZehQAU5uAbv2DDKd5LoSdpKOkSWLPfiL@jellyfish.rmq.cloudamqp.com/hbflrvwb')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def on_message(ch, method, properties, body):
    print('Received in admin')
    print(body)

channel.basic_consume('admin', on_message, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
