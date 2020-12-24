import pika, json
from main import Product, db

params = pika.URLParameters('amqps://hbflrvwb:ZehQAU5uAbv2DDKd5LoSdpKOkSWLPfiL@jellyfish.rmq.cloudamqp.com/hbflrvwb')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def on_message(ch, method, properties, body):
    print('Received in Main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created': 
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('Product Created')

    elif properties.content_type == 'product_updated':
        product = Product.query.get(data[id])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print('Product Updated')

    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print('Product Deleted')

channel.basic_consume('main', on_message, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
