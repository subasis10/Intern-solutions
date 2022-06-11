import csv
with open('csv-sample.csv','r') as file:
	table=csv.reader(file)
	count=0
	for line in table:
		count=count+1
	print("The number of lines is : "+ str(count))
