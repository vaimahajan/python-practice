# ----------
# Log Parser
# ----------
# Logic:
# 1. Open log file and read all IP addresses
# 2. Count qty of requests from each IP
# 3. Write evaluated data to csv

#!/usr/bin/python
import re
import csv
from collections import Counter

def reader(logfile):
	
	ip_regex=r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

	with open(logfile) as f:
		logs=f.read()
		iplist=re.findall(ip_regex,logs)
		return iplist

def ipcounter(ips):
	counts=Counter(ips)
	return counts
	#print counts.most_common(2)

def writer(ipinfo):
	with open('logoutput.txt','w') as output:
		writer=csv.writer(output)
		for key in ipinfo:
			writer.writerow((key,ipinfo[key]))


writer(ipcounter(reader('test.log')))