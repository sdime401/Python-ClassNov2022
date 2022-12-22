# This Python Code will retrieve all the EC2 instance in the account, generate a CSV file, upload the CSV to an S3 bucket, and send an email to a user.
import boto3
import logging
import csv
from botocore.exceptions import ClientError
from email.message import EmailMessage
from app import password
import ssl
import smtplib 

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger()


# Constant : Global variable
BUCKET = "simon-bucket-whvicif"
FILE_NAME= input("Please enter a name for your report: ")
FILE_NAME = FILE_NAME +".csv"
OBJECT_NAME = input("Please enter a descriptive S3 object name(This is the name your report will have in the S3 bucket): ") # The object name is the name that you want your file to have in the S3 bucket
OBJECT_NAME =OBJECT_NAME + ".csv"

def list_ec2_instance():
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    response = ec2_client.describe_instances()
    list_of_ec2=[]

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            server_name = instance['Tags'][0]['Value']
            instance_id= instance['InstanceId']
            image_id = instance['ImageId']
            instance_type = instance['InstanceType']
            public_address = instance['PublicIpAddress']
            security_id = instance['SecurityGroups'][0]['GroupId']

            list_of_ec2.append([server_name, instance_id, image_id, instance_type, public_address, security_id])
    return list_of_ec2


def generate_csv(data):
    """generate CSV file

    :param header: the columns that will control the table in CSV
    :param data: the list of EC2 parameters retrieved from the AWS account
    :return: Your report has successfully been created  if report was created, else file does not exist because of {error}
    """
    # CSV header
    header = ['server name', 'Instance ID', 'AMI ID', 'Instance type', 'Public Address', 'Security Group ID']
    try:
        with open(FILE_NAME, 'w', encoding='UTF8', newline='') as file:
            writer = csv.writer(file)

            # write the header
            writer.writerow(header)

            # write the data
            writer.writerows(data)
    except FileNotFoundError as error:
        logger.error(f"file does not exist because of {error} ")
        return False
    return True
    

def upload_to_S3_bucket():
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. The name that you want your file to have in S3
    :return: Your file has successfully been updated to S3!  if file was uploaded, else Your upload failed because of the following error {err}
    """


    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(FILE_NAME, BUCKET, OBJECT_NAME)
    except ClientError as err:
        logger.error(f"Your upload failed because of the following error {err}")
        return False
    return True 

def send_email():
    email_sender = "" #removed email for privacy. enter you sender email.
    # This is following password will allow you to authenticate to your sender email. You may generate it in your email settings
    email_password = password() # For security purpose, I have created another Environment variable and imported the password from there. 

    email_receiver = "simon.dime@yahoo.fr" # input("Please Enter the receiver email:  ") 

    subject = input("Please enter the subject of your email: ")
    link =input("Please enter the link of your object: ") 
    body = f"""
    Hello Sir, 

    Please find attached the link to download the report I generated.
    Link:  {link}

    Please let me know if you have any questions or concerns

    regards

    Simon

    """

    msg = EmailMessage()
    msg["From"] = email_sender
    msg["To"] = email_receiver
    msg["subject"] = subject
    msg.set_content(body)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, msg.as_string())
    except Exception as error2:
        return(f"The email has not been sent because of the following error: {error2}")



def send_sns():
    sns_client = boto3.client('sns',region_name='us-east-1' )
    link = input("Please enter the Object URL of your S3 object: ")
    response = sns_client.publish(
        TopicArn='arn:aws:sns:us-east-1:964920967101:my-sns-topic',
        Subject=input("Please Enter a Subject line: "),
        Message=f"""
    Hello Sir, 

    Please find attached the link to download the report I generated.
    Link:  {link}

    Please let me know if you have any questions or concerns

    regards

    Simon

    """
    )


if __name__ == "__main__":
    #logger= logging.info(f"Our EC2 list : {list_ec2_instance}")
    #print(list_ec2_instance())
    data = list_ec2_instance()
    generate_csv(data)
    logger.info(f"Your report {FILE_NAME} has successfully been created!")
    upload_to_S3_bucket()
    logger.info(f"Your {FILE_NAME} has successfully been uploaded as {OBJECT_NAME} to your {BUCKET} S3 bucket!")
    logger.info(f"You are now ready to send your email! Follow the steps as prompted.\n Dont forget to copy the link of the object in S3 to include in your email for your manager. ")
    #send_email()
    send_sns()
    logger.info(f"Your email has successfully been sent!")
    
