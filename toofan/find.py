import csv, operator
def find():
	a=0
	sample = open('allIndianTicker.csv', 'r')
	csv1=csv.reader(sample, delimiter=',')
	sort=sorted(csv1, key=operator.itemgetter(0))
	for l in sort:
		with open('sorted.csv') as f:
			if l[0] not in f.read():
				a = a+1
				print(l[0])
	return a
print(find())
