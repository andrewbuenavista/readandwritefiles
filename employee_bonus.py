import csv

employees = open("employeepay.csv",'r')

employee_file = csv.reader(employees,delimiter=',')

next(employee_file)

for employee in employee_file:

    pay = float(employee[3])
    bonus = float(employee[3]) * float(employee[4])
    total_pay = pay + bonus

    print("First Name: ", employee[1])
    print("Last Name:", employee[2])
    print("Salary:", f"{pay:<,.2f}")
    print("Bonus:",f"{bonus:<,.2f}")
    print("Total pay:",f"{total_pay:<,.2f}")

    print("")
    input("Press enter to continue: ")
