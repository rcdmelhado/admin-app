import configparser
import json

import django
import os
import pika

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

config = configparser.ConfigParser()
config.read('config.ini')
params = pika.URLParameters(config['rabbitmq']['uri'])

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()
