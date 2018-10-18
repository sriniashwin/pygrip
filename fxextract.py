# This script is meant to accept a date from the user and 
# return FX rates for USD, GBP, AUD, CHF, SGD and ZAR 
# based on data available in ECB

# The user provided date cannot lie more than 90 days in 
# the past, as the ECB xml does not contain this data

# Link to ECB XML: https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml?8222c213c2cab6b691d12745c85fcf3b

 
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen

import time

import xml.etree.ElementTree as ET #To be able to read XML format 
import ssl

import re
 
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

flag = 0
morentries = 1

requiredFX = ['USD']#, 'GBP', 'AUD', 'CHF', 'SGD', 'ZAR']

while (morentries == 1) :

	while (flag == 0):
		rawdate = input('Enter date in (YYYY-MM-DD) format- ')

		if (len(rawdate) == 0) :
			rawdate = '2018-10-10'
			print('Using default date as', rawdate)
			flag = 1	
		elif (len(rawdate) != 10) :
			print('Incorrect date entered, try again')
			flag = 0
			continue
		else : 
			flag = 1

	#pydate = time.strptime(rawdate, "%d/%m/%Y")

	#print (pydate)


	# url for extraction from ECB
	url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml?8222c213c2cab6b691d12745c85fcf3b"

		
	data = urlopen(url, context=ctx).read().decode()
	f = open("data.txt","a+") #create add file in write

	#f.close

	print('test1')

	#print('Received', len(data), 'characters') 

	content = ET.fromstring(data)
	#print(content[0],'\n',content[1],'\n',content[2])

	for child in content[2] :
		loopdate = child.attrib['time']
		if (loopdate != rawdate) :
			continue
		else :
			for subchild in child :
				if (subchild.attrib['currency'] in requiredFX) :
					print (rawdate, ':', subchild.attrib['currency'],':',subchild.attrib['rate'])
					f.write(rawdate)
					f.write(':')
					f.write(subchild.attrib['currency'])
					f.write(':')
					f.write(subchild.attrib['rate'])
					f.write('\n')
	f.close
	
	option = input('Do you want to fetch rates for more dates? (Y/n):')
	if ((len(option) == 0) or (option == "Y") or (option == "y"))  :
		morentries = 1
		flag = 0
	else :
		morentries = 0
