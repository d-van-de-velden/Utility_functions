import numpy as np 
import matplotlib.pyplot as plt 
import scipy as sci
import pandas as pd
import os, locale, csv, this
import dv_loadingBar

# Define the working directory and identify all files
fpath = '/workspace/myFirstTry/'
files = os.listdir(fpath)
print(files)

# Define a file ending to look out for
str_true = '.csv'

# Start an empty list to be filled in for loop on the condition of file-ending 
fnames = []
count = 0
for f in np.arange(len(files)):
    #print(f)
    tmp_fend = os.path.splitext(files[f])
    #print(tmp_fend[1])
    if tmp_fend[1] == str_true:
        if count == 100:
            break
        print(count)
        fnames.append(files[f])
        count = count +1

# Feedback on all filenames that have defined file ending
print(fnames)

# Define the columns/indeces of interest
col_list = ['Cars', 'Income']

# Loop over each defined column and then all files, while appending 
# an empty array with information from all the files 
# Done for all columns/indeces 
data_dict = dict()
for icol in range(len(col_list)):
    dv_loadingBar(icol, len(col_list))

    # Fill that array "index_data"
    index_data = np.empty([1,1])
    for fe in range(len(fnames)):
        # read csv files specifically for each column index
        pd_dat = pd.read_csv(fnames[fe], delimiter=';', usecols=[col_list[icol]]) # , usecols=['col1', 'col3', 'col7'])
        dat  = pd_dat.values
                
        # make np data array from string input of csv
        if ',' in dat[0][0]:
            mydata = np.empty(dat.shape)
            for ii in range(len(dat)):
                mydata[ii] = float(dat[ii][0].replace(',','.'))
        else:
            mydata = dat
            print('data was in nice format.')

        
        index_data = np.append(index_data, mydata, 0)
    
    print('Done with all files for index : ' + col_list[icol])


    print('Normalizing it.... : zscoring')
    index_data = index_data[1:]
    store_data = sci.stats.zscore(index_data)

    data_dict.update({col_list[icol]: store_data})

fname_save = '/workspace/myFirstTry/binary_file_from_csv.bin'
store_data.tofile(fname_save, sep='', format='%s')

loaded_list = np.fromfile(fname_save, dtype=float, count=- 1, sep='', offset=0, like=None)

    #fb = open(r'/workspace/myFirstTry/binary_file_from_csv.bin', 'wb')
    #store_data_b = bytearray(store_data)
    #fb.write(store_data)
    #fb.close()

    #fc = open(r'/workspace/myFirstTry/binary_file_from_csv.bin', 'rb')
    #l = list(fc.read())
    #loaded_list = np.float(l)







#A = np.random.randint(1,50, [10,10])
#x = np.linspace(1,10,10)
#print(A[1,:])
#print('X : ' + str(x[:]))

#fig, ax = plt.subplots(1,1)
#ax.plot(x, A[1,:])
#plt.show()
#plt.savefig('example_plot.png', dpi=150)

#fig, ax = plt.subplots(1,1)
#ax.plot(x, A[1,:])
#plt.show()
#plt.savefig('example_plot.png', dpi=150)