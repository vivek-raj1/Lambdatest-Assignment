from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import boto3
import argparse
import logging
import time
from botocore.client import Config
parser = argparse.ArgumentParser(description='Please Provide the URL')
parser.add_argument('-u','--url',help='url', required=True)
args = parser.parse_args( )
chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument('--headless')
chrome_opt.add_argument('--no-sandbox')
driver =  webdriver.Chrome('./chromedriver', options=chrome_opt)
driver.get(args.url)
sleep(2)
a = time.strftime("%Y%m%d%H%M%S")
filename= a+"crome.png"
driver.get_screenshot_as_file(filename)
print ("...END..")
driver.close()
session = boto3.Session(profile_name="vivek")
region="ap-south-1"
bucket_name="vivek-lambda-test"
s3_client = session.client('s3',region_name=region,config=Config(s3={'addressing_style': 'path'}, signature_version='s3v4'))
try:
        response = s3_client.upload_file(filename, bucket_name, filename)
except :
        print("connection failed to s3")
object_url = "https://"+bucket_name+".s3."+region+".amazonaws.com/"+filename
response_url = s3_client.generate_presigned_url('get_object',Params={'Bucket': bucket_name,'Key': filename},ExpiresIn=3600)
print(response_url)
