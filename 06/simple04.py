import csv

output_list = ['1','2','3','4']


with open('D:\\Python\\06\\test.csv','a+') as csvfile:
    
    w = csv.writer(csvfile)

    w.writerow(output_list)