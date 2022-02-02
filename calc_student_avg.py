import csv

student = open('student_scores.csv','r')
student_avg = open('student_avg.csv','w',newline='')

student_file = csv.reader(student,delimiter=',')
student_avg_file = csv.writer(student_avg,delimiter=',')

student_avg_file.writerow(["Name","Average"])

for record in student_file:

    avg = (int(record[1]) + int(record[2]) + int(record[3])) / 3
    student_avg_file.writerow([record[0],f"{avg:.2f}"])