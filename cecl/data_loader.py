# data set credits to : https://www.kaggle.com/datasets/adarshsng/lending-club-loan-data-csv

# code theory credits to :https://in.mathworks.com/content/dam/mathworks/white-paper/cecl-and-ifrs-9-modeling-in-matlab-qa.pdf
#further clarifications were sought from https://www2.deloitte.com/us/en/pages/audit/articles/us-current-expected-credit-losses-cecl-implementation-insights.html
#and https://www.investopedia.com/terms/r/roll-rate.asp
import os
import csv
import machine_learning.data_loader as data_loader
dirname = os.path.dirname(__file__)
relative_path_to_file = '../data/original_files/kaggle/loan.csv'

#the following file reading module can be loaded to a different function since we do it multiple times
filename = os.path.join(dirname, relative_path_to_file)
data = data_loader(filename)
print(len(data))


no_of_smaller_files = 5
no_of_entries_per_file = int(len(data) / no_of_smaller_files)
subdata = data[0:no_of_entries_per_file]
relative_path_to_out_file = '../data/preprocessed_files/kaggle/loan_short.csv'
fullpath_to_outfile = os.path.join(dirname, relative_path_to_out_file)



with open(fullpath_to_outfile,'w+') as file:
    writer = csv.writer(file)
    writer.writerows(subdata)


