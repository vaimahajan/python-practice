#!/usr/bin/python

import string
import random

def id_generator(size=9, chars=string.ascii_letters + string.digits):
	result=0
	while result is not 1:
		password=''.join(random.choice(chars) for _ in range(size))
		for i in password:
			if i.isdigit():
				result=1
				print password
				return

id_generator()