import csv

customers = open('customers.csv','r')

customer_file = csv.reader(customers, delimiter=',')

#to skip a line if the file contains a header record
next(customer_file)

for record in customer_file:
    print("Last Name:",record[2])
