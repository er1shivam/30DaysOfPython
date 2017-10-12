#  Simple templates
import csv



with open("data.csv", "w+" , newline=""):
    writer = csv.writer(csvfile)
    writer.writerow(["col1","col2"])
    writer.writerow(["data1","data2"])

with open("data.csv", "r"):
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv", "a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["data 3","data 4"])


with open("data.csv", "a", newline="") as csvfile:
    fieldnames = ["id","title"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames
    writer.writerow({"id": 123, "title": "New Title"})