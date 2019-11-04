from distutils.core import setup

setup(
    name='notificationhub-sdk',
    version='0.1.0',
    packages=['notificationhub-sdk', ],
    author='Raghav Nayak',
    author_email='raghavendra.nayak@olxpeople.com',
    description='Notification Hub provides sdk to push the message to Amazon SQS',
    long_description=open('README.md').read(),
    url='https://github.com/aasaanjobs/notification-hub-py-sdk',
    install_requires=[
        "boto3==1.10.4",
        "botocore==1.13.4",
        "protobuf==3.10.0",
    ],
)
