#!/usr/bin/env python3

import json
from connection import Connection
from queuing import Producer



class ProductsConnection(Connection):
	def query_callback(self):
		producer = Producer("products_data")

		products =  self.query("select id, name, price from product;")
		result = [{"id": p[0], "name": p[1], "price": p[2]} for p in products]
		producer.publish(json.dumps(result))
		print(products)