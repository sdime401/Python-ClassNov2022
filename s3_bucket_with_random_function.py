import boto3
import random
import string
def create_unique_bucket_name(bucket_prefix):
    '''
    This function create an s3 bucket with given bucket prefix, and a random sequence of characters.
    
    Parameters:
    string: gets the bucket prefix
  
    Returns:
    returns a unique name bucket_prefix+7-char-long random string
    
    '''
    N = 7
    # using random.choices()
    # generating random lowercase strings
    rand_string= ''.join(random.choices(string.ascii_lowercase, k=N))

    return "-".join([bucket_prefix, str(rand_string)])

bucket_prefix="simon-bucket"

s3_client = boto3.client('s3')
response=s3_client.create_bucket(
    Bucket=create_unique_bucket_name(bucket_prefix),
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-1',
    }
)
print(response)
