import csv

with open('D:\\Python\\06\\test.csv','r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)
        print(row[0])