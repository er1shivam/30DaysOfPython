import csv
# Write and reading from csv
with open("data.csv", "w+" , newline=""):
    writer = csv.writer(csvfile)
    writer.writerow(["col1","col2"])
    writer.writerow(["data1","data2"])

with open("data.csv", "r"):
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)