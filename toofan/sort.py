import csv, operator
def sort():
	sample = open('fincode.csv', 'r')
	csv1=csv.reader(sample, delimiter=',')
	sort=sorted(csv1, key=operator.itemgetter(0))
	wr=open('sorted.csv', 'w')
	for l in sort:
		print(l[0])
		a=l[0]
		b=l[1]
		c=(a+','+b)
		wr.write(str(c))
		wr.write('\n')

sort()
