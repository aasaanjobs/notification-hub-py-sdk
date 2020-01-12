# Python Aasaanjobs Notification Hub Client

[![Build Status](https://travis-ci.org/aasaanjobs/notification-hub-py-sdk.svg?branch=master)](https://travis-ci.org/aasaanjobs/notification-hub-py-sdk)
[![codecov](https://codecov.io/gh/aasaanjobs/notifications-python-sdk/branch/master/graph/badge.svg)](https://codecov.io/gh/aasaanjobs/notifications-python-sdk)

Official low-level client for communicating with central notification hub. Its goal is to provide common ground for 
all notification-related code in Python.

## What is Notification Hub?

The Notification Hub is intended to be a backend micro-service to handle all notifications being sent to end users 
from the system. This micro-service should be the sole handler of sending notification tasks to proper 3rd party 
notification service providers along with parsing and validating the content of the notifications.

## Supported Notification Channels

The following channels of communication are supported by this SDK
- Simple Messaging Service (SMS)
- Email
- WhatsApp
- Mobile Push (FCM)

## Installation
Install the `aasaanjobs-notificationhub` using pip:
```shell script
pip install aasaanjobs-notificationhub
```

## Overview

Each notification is referred to as **Task** in this library. A single **Task** can contain
multiple channels, i.e., a single **Task** can contain both **Email** and **WhatsApp** notification data.
This **Task** is then validated via [Protocol Buffers](https://developers.google.com/protocol-buffers)
and pushed to corresponding Notification Hub Amazon SQS queue.

## Configuration

Each application which uses this library must configure Amazon SQS configurations to successfully
send notification task to Hub.

The following keys can be defined in the settings module if Django application or can be defined as environment variables

| **Setting**                            | **Description**                                                   |
|----------------------------------------|-------------------------------------------------------------------|
| NOTIFICATION_HUB_SQS_ACCESS_KEY_ID     | Access Key of the IAM role which has access to the Hub SQS        |
| NOTIFICATION_HUB_SQS_SECRET_ACCESS_KEY | Secret Access Key of the IAM role which has access to the Hub SQS |
| NOTIFICATION_HUB_SQS_REGION            | AWS Region where the Hub SQS resides                              |
| NOTIFICATION_HUB_SQS_QUEUE_NAME        | Name of the Hub SQS Queue                                         |

## Example Usage
The following code snippet provides an example of sending an SMS to notification hub.
```python
from notificationhub_sdk import Sms, Task
from notificationhub_sdk.common import MessageType, Platform


if __name__ == '__main__':
    # Create a SMS object
    sms = Sms(
        send_to='888888888', 
        template='https://olx-notifications.aasaanjobs.com/production/aasaanjobs/blank_sms_template.html',
        context={'html': 'This is test SMS'}
    )
    # Create a notification task
    task = Task(
        name='test_sms', sent_by_id='123456', client='cts', platform=Platform.Aasaanjobs,
        message_type=MessageType.TRANSACTIONAL, sms=sms
    )
    # Send task to SQS
    task.send()
```
