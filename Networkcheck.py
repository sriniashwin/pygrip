# Program meant to ping google.com every 5 minutes and store the result (ping success/failure) in a text file

import os
import datetime
import time
import subprocess



def ping():
	hostname = "google.com"

	proc = subprocess.Popen(['ping',hostname],stdout = subprocess.PIPE)
	stdout, stderr = proc.communicate()
	
	if proc.returncode == 0: # successful ping
		response = 1 # connection is on
	else: # unsuccessful ping, returncode = 2
		response = 0 # connection is off
	#response = os.system("ping " + hostname)

	#if response == 0:
	#	status = 0
		#print(datetime.datetime.now(), ":", status)
		
	#else:
	#	status = 1
		#print(datetime.datetime.now(), ":", status)
	
	#create add file in write
	
	print(datetime.datetime.now(),"Writing to file..")
	f = open("connectionstatus.txt","a+") 
	f.write(str(datetime.datetime.now()))
	f.write(":")
	f.write(str(response))
	f.write('\n')
	f.close

try:		
	while(True):
		time.sleep(300)
		ping()
except KeyboardInterrupt:
	exit
		
