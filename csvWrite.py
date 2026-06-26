import csv

name = input("What's ur name? ")
home = input("Where's ur home? ")

with open("students.csv", "a") as file:
  writer = csv.DictWriter(file, fieldnames=["name", "home"])
  writer.writerow({"home": home, "name": name})
