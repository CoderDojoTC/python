import os
# sample code taken from: https://stackoverflow.com/questions/2953462/pinging-servers-in-python
# This will the Unix "ping" command which will work from most Mac and UNIX systems but not on Windows
hostname = "127.0.0.1" # example of pinging the loopback address
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print(hostname, 'is up!')
else:
  print(hostname, 'is down!')
