
import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://hbflrvwb:ZehQAU5uAbv2DDKd5LoSdpKOkSWLPfiL@jellyfish.rmq.cloudamqp.com/hbflrvwb')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def on_message(ch, method, properties, body):
    print('Received in admin')
    data = json.loads(body)
    print(data)
    product = Product.objects.get(id=data)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased')

channel.basic_consume('admin', on_message, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
