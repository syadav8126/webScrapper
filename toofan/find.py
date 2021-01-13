import csv, operator
def find():
	sample = open('allIndianTicker.csv', 'r')
	csv1=csv.reader(sample, delimiter=',')
	sort=sorted(csv1, key=operator.itemgetter(0))
	for l in sort:
		with open('sorted.csv') as f:
			if l[0] not in f.read():
				a=1
				print(l[0])
find()
