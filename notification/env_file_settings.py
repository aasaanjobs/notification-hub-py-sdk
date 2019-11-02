import os
from pathlib import Path
from dotenv import load_dotenv

SQS_ACCESS_KEY_ID = None
SQS_SECRET_ACCESS_KEY = None
SQS_QUEUE_URL = None
SQS_REGION = None


def load_sqs_settings() -> bool:
    return_val = False
    # need to place .env file in the same directory
    load_dotenv(verbose=True)

    global SQS_ACCESS_KEY_ID
    global SQS_SECRET_ACCESS_KEY
    global SQS_QUEUE_URL
    global SQS_REGION

    SQS_ACCESS_KEY_ID = os.getenv("SQS_ACCESS_KEY_ID")
    SQS_SECRET_ACCESS_KEY = os.getenv("SQS_SECRET_ACCESS_KEY")
    SQS_QUEUE_URL = os.getenv("SQS_QUEUE_URL")
    SQS_REGION = os.getenv("SQS_REGION")

    if SQS_ACCESS_KEY_ID is not None \
            and SQS_SECRET_ACCESS_KEY is not None \
            and SQS_QUEUE_URL is not None \
            and SQS_REGION is not None:
        return_val = True
    else:
        print("Error while getting SQS settings from .env file")

    return return_val
