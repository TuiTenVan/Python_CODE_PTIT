import csv

def doc(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[5].strip())

if __name__ == "__main__":
    file = 'addresses.csv'
    doc(file)