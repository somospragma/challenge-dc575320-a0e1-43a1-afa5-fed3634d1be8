import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


def get_aws_credentials() -> dict:
    """Retrieve AWS credentials from environment variables.

    Returns:
        dict: A dictionary containing the AWS access key ID and secret access key.
    """    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

    if not aws_access_key_id or not aws_secret_access_key:
        raise NoCredentialsError('AWS credentials not found in environment variables.')

    return {
        'aws_access_key_id': aws_access_key_id,
        'aws_secret_access_key': aws_secret_access_key
    }


def get_aws_session() -> boto3.session.Session:
    """Create an AWS session using the retrieved credentials.

    Returns:
        boto3.session.Session: An AWS session object.
    """    credentials = get_aws_credentials()

    try:
        session = boto3.Session(
            aws_access_key_id=credentials['aws_access_key_id'],
            aws_secret_access_key=credentials['aws_secret_access_key']
        )
    except (NoCredentialsError, PartialCredentialsError) as e:
        raise e

    return session


def get_bedrock_client() -> boto3.client:
    """Create a Bedrock client using the AWS session.

    Returns:
        boto3.client: A Bedrock client object.
    """    session = get_aws_session()
    return session.client('bedrock')