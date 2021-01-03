import csv

a_file = open("sample.csv", "w")
a_dict = {"a": 1, "b": 2}
writer = csv.writer(a_file)
for key, value in a_dict.items():
    writer.writerow([key, value])
a_file.close()



