# with open("students.csv") as file:
#   for line in file:
#     name, house = line.rstrip().split(",")
#     print(f"{name} is in {house}")
import csv
students = []

# with open("students.csv") as file:
#   for line in file:
#     name, house = line.rstrip().split(",")
#     student = {"name": name, "house": house}
#     students.append(student)
    
# def get_name(student):
#   return student["name"]

# with open("students.csv") as file:
#   reader = csv.DictReader(file)
#   for row in reader:
#     students.append({"name": row["name"], "home": row["home"]})

with open("students.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    students.append(row)

# for student in sorted(students, key=lambda student:student["name"]):
#   print(f"{student['name']} is in {student['house']}")

for student in sorted(students, key=lambda student:student["name"]):
  print(f"{student['name']} is from {student['home']}")