#!/usr/bin/env python3
import json
import schedule
import time
from web_service_client import WebServiceClient
from xml.etree import ElementTree as ET
from queuing import Producer


class ProductsWebServiceClient(WebServiceClient):
	def parse_xml(self, xml):
		root = ET.fromstring(xml)

		return {
			"id": int(root.find("id").text),
			"name": root.find("name").text,
			"price": float(root.find("price").text),		
		}
	

	def get_products(self):
		response = self.call_api()
		products = [self.parse_xml(product) for product in response]

		return products

	
	def read_and_dump(self):
		producer = Producer("products_data")
		products = self.get_products()

		content = json.dumps(products)
		producer.publish(content)
		print("Products were successfully published.")
		print(products)
		


	def schedule_job(self, time_interval=10):
		self.read_and_dump()

		schedule.every(time_interval).seconds.do(self.read_and_dump)

		while(True):
			schedule.run_pending()
			time.sleep(time_interval)
		
		

