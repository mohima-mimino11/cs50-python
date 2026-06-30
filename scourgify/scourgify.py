import sys
import csv



if len(sys.argv) < 2:
  sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
  sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv"):
  sys.exit("Not a CSV file")
try:
  with open(sys.argv[1]) as inp_file:
    reader = csv.DictReader(inp_file)
    with open(sys.argv[2], "w") as out_file:
      writer = csv.DictWriter(out_file, fieldnames=["first", "last", "house"])
      writer.writeheader()
      for row in reader:
        last, first = row["name"].split(", ")
        writer.writerow({"first": first, "last": last, "house": row["house"]})

except FileNotFoundError:
  sys.exit("Could not read invalid_file.csv")
