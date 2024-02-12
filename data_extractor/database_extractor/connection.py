#!/usr/bin/env python3

from sqlalchemy import create_engine, text
import schedule
import time


class Connection():
	def __init__(self, db_url):
		self.__engine =  create_engine(db_url)
		

	def query(self, query_string):
		with self.__engine.connect() as connection:
			return connection.execute(text(query_string)).all()
		

	def query_callback(self):
		pass
	

	def schedule_query(self, time_in_seconds=10):
		self.query_callback()

		schedule.every(time_in_seconds).seconds.do(self.query_callback)

		while(True):
			schedule.run_pending()
			time.sleep(time_in_seconds)
	
		
	