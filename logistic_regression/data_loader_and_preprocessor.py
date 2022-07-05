import os
import numpy as np
relative_path_to_data = '../data/preprocessed_files/uci_archives/data_banknote_authentication.txt'
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, relative_path_to_data)

def data_loader(file_n):
    file = open(file_n, 'r')
    lines = file.readlines()
    file.close()
    return lines

def data_cleaner(lines):
    lines = [l.replace('\n','') for l in lines]
    lines= [l.split(',') for l in lines]
    data = []
    label = []
    [data.append(l[0:-1]) for l in lines]
    [label.append(l[-1]) for l in lines]
    X,y = (data,label)
    print(len(lines))
    print(lines[0])
    return X,y

lines = data_loader(filename)
X,y = data_cleaner(lines)
X = np.array(X).astype(np.float)
y = np.array(y).astype(np.float)
