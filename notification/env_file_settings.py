import os
from pathlib import Path
from dotenv import load_dotenv


def load_sqs_settings() -> dict:
    sqs_config = dict()
    # need to place .env file in the same directory
    load_dotenv(verbose=True)

    sqs_config['SQS_ACCESS_KEY_ID'] = os.getenv("SQS_ACCESS_KEY_ID")
    sqs_config['SQS_SECRET_ACCESS_KEY'] = os.getenv("SQS_SECRET_ACCESS_KEY")
    sqs_config['SQS_QUEUE_URL'] = os.getenv("SQS_QUEUE_URL")
    sqs_config['SQS_REGION'] = os.getenv("SQS_REGION")

    if sqs_config['SQS_ACCESS_KEY_ID'] is  None \
            and sqs_config['SQS_SECRET_ACCESS_KEY'] is None \
            and sqs_config['SQS_QUEUE_URL'] is None \
            and sqs_config['SQS_REGION'] is None:
        print("Error while getting SQS settings from .env file")

    return sqs_config
