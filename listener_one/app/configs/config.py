from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file once

RABBITMQ_URL = os.getenv("RABBITMQ_URL")
SERVICE_A_URL = os.getenv("SERVICE_A_URL")
# RabbitMQ Queue and Exchange Names
QUEUE_NAME = os.getenv("QUEUE_NAME")  # Default to queue_a_task if not specified
RESULT_EXCHANGE_NAME = os.getenv("RESULT_EXCHANGE_NAME")
TASK_EXCHANGE_NAME = os.getenv("TASK_EXCHANGE_NAME", "gateway_fanout_exchange") 


