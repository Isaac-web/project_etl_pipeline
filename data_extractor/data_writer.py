#!/usr/bin/env python3

from motor.motor_asyncio import AsyncIOMotorClient
import json


class DataWriter():
	def __init__(self):
		self.client = AsyncIOMotorClient("mongodb://127.0.0.1")
		self.db = self.client["etl_db"]
		self.products_collection = self.db.products
		

	
	async def do_find_products(self):
		cursor = self.products_collection.find()
		for product in await cursor.to_list(10):
			print(product)



	async def insert_products(self, data):
		try:
			parsed_data = json.loads(data)

			response = await self.products_collection.insert_many(parsed_data)
			print("{0} entities were inserted into the data store.".format(len(response.inserted_ids)))
		except Exception as e: 
			print("Something went wrong while parsing the data into json.")


	def do_insert_products(self, data):
		loop = self.client.get_io_loop()
		loop.run_until_complete(self.insert_products(data))


		
