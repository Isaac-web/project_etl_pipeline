#!/usr/bin/env python3

from products_connection import ProductsConnection
from queuing import Producer, Consumer


def init():
	connection = ProductsConnection("mysql://takiy:password@localhost/elt_test_db")
	connection.schedule_query(5)


if __name__ == "__main__":
	init()





	


	