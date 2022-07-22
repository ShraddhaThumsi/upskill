import csv
def get_data(filename):
    file = open(filename)
    csvreader = csv.reader(file)
    data = []
    for row in csvreader:
        data.append(row)

    file.close()
    return data