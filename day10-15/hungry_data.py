import csv

def get_length(file_path):
    with open(file_path , "r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)

def append_data(file_path,name,email):
    fieldnames = ["id","name","email"]
    next_id = get_length(file_path)
    with open("data.csv", "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()        
        writer.writerow({
            "id": next_id,
            "name": name,
            "email": email,
            })

append_data("data.csv","shivam","er1shivam@gmail.com")