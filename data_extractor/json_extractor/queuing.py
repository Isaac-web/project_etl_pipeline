#!/usr/bin/env python3
import pika

class Producer():
	def __init__(self, queue_name, host="127.0.0.1"):
		self.__queue_name = queue_name
		self.__connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
		self.__channel = self.__connection.channel()
		self.__channel.queue_declare(queue_name)


	def __def__(self):
		self.__connection.close()


	def publish(self, data):
		self.__channel.basic_publish(exchange="", routing_key=self.__queue_name, body=data)
		print("Message sent successfully.")


class Consumer():
	def __init__(self, queue_name, host="127.0.0.1"):
		self.__queue_name = queue_name
		self.__connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
		self.__channel = self.__connection.channel()
		self.__channel.queue_declare(queue_name)


	def __del__(self):
		self.__connection.close()


	def callback(self, ch, method, properties, body):
		print(body)
		ch.basic_ack(delivery_tag=method.delivery_tag)


	def consume(self):
		print("Reading messages...")

		self.__channel.basic_consume(queue=self.__queue_name, 
							   on_message_callback=self.callback)
		self.__channel.start_consuming()
