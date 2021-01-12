import re
f1=open("symbollink.csv")
f2=open("symbollink1.csv",'w')
for line in f1.readlines():
	x=re.findall('^"',line)
	if not x:
		print(line)
		f2.write(line)
