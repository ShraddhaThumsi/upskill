file_name = '../data/rbi/crop_turnout.txt'
outfile_path = '../data/rbi/crop_data_pairs.csv'
print('filename is:')
print(file_name)
import csv
def read_data_from_file(f):
    print('in read data function')
    file = open(f,'r')
    print('opened file')
    lines = file.readlines()
    lines= [l.replace('\n','').replace(',','').replace('\'','').replace(' ','') for l in lines]
    lines = [l.split('\t') for l in lines]
    file.close()
    return lines
print('about to call read data function')
all_data = read_data_from_file(file_name)
headers = all_data[0]
data = all_data[1:]
def prepare_data_pairs(headers, vals,crop='Rice'):
    data_set = []
    rice_index = headers.index(crop)
    total_cereals_index = headers.index('TotalCereals')
    total_foodgrans_index = headers.index('TotalFoodgrains')
    for v in vals:
        rice_value = v[rice_index]
        totalcereals_value = v[total_cereals_index]
        total_foodgrains_value = v[total_foodgrans_index]
        data_point = (rice_value,totalcereals_value,total_foodgrains_value)

        data_set.append(data_point)
    return data_set

def prepare_data_rows(vals):
    data_set = []
    index_range_start = 1
    index_range_stop = 5
    for v in vals:
        row = v[index_range_start:index_range_stop]
        data_set.append(row)
    return data_set

print(headers)
print(data[1])

#data_pairs = prepare_data_pairs(headers,data,'Rice')
data_pairs = prepare_data_rows(data)
for p in data_pairs:
    print(p)

with open(outfile_path,'w') as file:
    writer = csv.writer(file)
    writer.writerows(data_pairs)

