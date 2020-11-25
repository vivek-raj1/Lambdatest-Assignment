from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1024, 768))
display.start()
import time
import argparse
parser = argparse.ArgumentParser(description='Please Provide the URL')
parser.add_argument('-u','--url',help='url', required=True)
args = parser.parse_args( )
import boto3
from botocore.client import Config
options = Options()
options.headless = True
capabilities = webdriver.DesiredCapabilities().FIREFOX
capabilities["marionette"] = True
binary = FirefoxBinary('/usr/bin/firefox')
driver = webdriver.Firefox(firefox_binary=binary,capabilities=capabilities,options=options,executable_path='/usr/local/bin/geckodriver')
driver.get(args.url)
print("_____START____")
a = time.strftime("%Y%m%d%H%M%S")
filename= a+"firefox.png"
driver.get_screenshot_as_file(filename)
driver.close()
display.stop()
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
