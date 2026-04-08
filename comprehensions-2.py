import re
import csv

def get_words(filename):
  with open(filename, "r") as f:
    contents = f.read()
  contents = " ".join(contents.split())
  contents = re.sub(r"[^\w\- ]", "", contents)
  contents = re.sub(r"\-\-", " ", contents)
  return contents.split()

def save_counts(counts):
  with open("counts.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Word", "Count"])
    for word, count in sorted(counts.items(), key = lambda x : x[1], reverse = True):
      writer.writerow([word, count])

def main():
  counts = {}
  words = get_words("address.txt")
  lowercase_words = [word.lower() for word in words if len(word) > 4]
  counts = {word: words.count(word) for word in lowercase_words}
  save_counts(counts)
  
main()