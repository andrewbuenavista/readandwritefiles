import csv

customers = open('customers.csv','r')
customer_country = open('customer_country.csv','w',newline='')

customer_file = csv.reader(customers, delimiter=',')
country_file = csv.writer(customer_country, delimiter=',')

#to skip a line if the file contains a header record
next(customer_file)

country_file.writerow(["First Name", "Last Name", "Country"])

count = 0

for record in customer_file:
    country_file.writerow([record[1],record[2],record[4]]) 
    count += 1

print(count)   