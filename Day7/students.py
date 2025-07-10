import csv
# students = []
# with open("students.csv") as file:
#     # for line in file:
#     #     name,home = line.rstrip().split(",")
#     #     student = {"name" : name,"home" : home}
        
#     #     students.append(student)
#     # reader = csv.reader(file)
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name" : row["name"] , "home" : row["home"]}) 
# def get_name(student):
#     return student["name"]

# def get_house(student):
#     return student["home"]

# for student in sorted(students,key=lambda student : student["name"]):
#     print(f"{student['name']} is in {student['home']}")

name = input("What's your name ? ")
home = input("Where's your home ? ")

with open("students.csv","a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name" : name , "home" : home})