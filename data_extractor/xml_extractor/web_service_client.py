#!/usr/bin/env python3
from zeep import Client


class WebServiceClient():
	def call_api(self):
		client = Client("http://localhost:8000/?wsdl")
		try:
			try:
				return client.service.get_all_products()
			except Exception:
				print("Something went wrong while calling the SOAP.")
		except Exception:
			print("Something went wrong.")