relative_path_to_data = '../data/preprocessed_files/kaggle/loan_sub.csv'
#the loan_sub file has been left out of git because its size exceeds 100mb.
# In case you would like to run the code on the same data as I, please reach out to me at
#thumsishraddhasatish@gmail.com, I will be happy to share the file with you.
# if you would like to download the original data from Kaggle, it can be found at https://www.kaggle.com/datasets/adarshsng/lending-club-loan-data-csv

import os
import pandas as pd
import machine_learning.data_loader as data_loader
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, relative_path_to_data)

data = data_loader.get_data(filename)
print(len(data))
df = pd.read_csv(filename)
colnames_for_rollingdelinq = ['num_tl_30dpd','num_tl_90g_dpd_24m','num_tl_120dpd_2m']
# for c in colnames_for_rollingdelinq:
#     print(c in data[0])