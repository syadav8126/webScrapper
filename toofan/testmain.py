from testing import spiderController
import time
import sys
from testing import duplicate
import subprocess

global s
global e
s=200000
e=200050
'''
with open("fincode.csv", 'r') as fl:
	for a in fl:
		d,d1=a.split(',')
		s=int(d1)-10
		e=int(d1)+10
		subprocess.call([sys.executable, './testing.py',str(s),str(e)])
		time.sleep(50)
		
'''
for i in range(1,100):
	subprocess.call([sys.executable, './testing.py',str(s),str(e)])
	time.sleep(50)
	s=s+50
	e=e+50
	duplicate()
