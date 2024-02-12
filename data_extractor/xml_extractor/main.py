#!/usr/bin/env python3

from products_web_service_client import ProductsWebServiceClient


if __name__ == "__main__":
	client = ProductsWebServiceClient()
	client.schedule_job(5)
	