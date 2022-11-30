from google.cloud import logging
import random

def hello_world (request):

	logging_client = logging.Client()

	logger = logging_client.logger("monitoring-training-1")

	logger.log_struct(
	{"data": {"ratesPerSecond": {"price": random.randint(0,5)}}}
	)

	print("Wrote logs to {}.".format(logger.name))



	logger2 = logging_client.logger("monitoring-training-2")

	logger2.log_struct(
	{"data": {"market": {"open": 0 }}}
	)

	print("Wrote logs to {}.".format(logger2.name))

	return f"hecho!"
