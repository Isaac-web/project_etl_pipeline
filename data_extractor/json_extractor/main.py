#!/usr/bin/env python3

import json
import schedule
import time
from queuing import Producer


class JSONReader():
	def __init__(self, path):
		self.path = path


	def read_and_dump(self):
		producer = Producer("products_data")
		content = self.read()
		producer.publish(json.dumps(content))
		print(content)



	def read(self):
		with open(self.path, "r") as file:
			return json.load(file)


	def schedule_job(self, time_interval = 5):
		self.read_and_dump()

		schedule.every(time_interval).seconds.do(self.read_and_dump)


		while(True):
			schedule.run_pending()
			time.sleep(time_interval)



if __name__ == "__main__":
	reader = JSONReader("data.json")

	content = reader.schedule_job(3)
	
