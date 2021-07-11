# Created by Jash Shah.
# Date : 08/07/21

import scipy.io as io
import numpy as np
import random
import math

# Loading the original file
orig_file = io.loadmat("C:/Users/Jash Shah/Desktop/BCI_Assignment/data.mat")
labels = orig_file["labels"]
print("\nShape of the original labels",labels.shape)
data = orig_file["trials"]
print("\nShape of the original data",data.shape)

# Making duplicates
dup_lab = labels
dup_data = data
noise = np.random.normal(0, .1, dup_data.shape)
addition = noise + dup_data
print("\nShape of the noisy data",addition.shape)

# Adding noise and concatenating the files
Labels = np.append(dup_lab, labels, axis = 1)
print("\nShape of the combined labels",Labels.shape)
Data = np.append(addition, data, axis = 0)
print("\nShape of the combined data",Data.shape)

# Shuffling the data
tab = []
for num,i in enumerate(Labels[0]):
	tab.append( [Data[num] , i] )
tab = np.asarray(tab)
np.random.shuffle(tab)
print(tab.shape)

# Randomly removing rows
randomlist = []
for i in range(17):
	n = random.randint(0,799)
	randomlist.append(n)
tab = np.delete(tab, randomlist, axis=0)
print(tab.shape)

# Splitting the data
index = math.floor(len(tab)*0.7) 		# 70 - 30 split
train_data = tab[:index]
test_data = tab[index:]
print(train_data.shape)					# 548
print(test_data.shape)					# 235

# Making the dictionary
Train_data = []
Train_labels = []
Test_data = []
Test_labels = []

for i in train_data:
	Train_data.append(i[0])
	Train_labels.append(i[1])
Train_labels = np.asarray(Train_labels)
Train_data = np.asarray(Train_data)
print("train_data = ", np.asarray(Train_labels).shape, "\t", np.asarray(Train_data).shape)

for i in test_data:
	Test_data.append(i[0])
	Test_labels.append(i[1])
Test_labels = np.asarray(Test_labels)
Test_data = np.asarray(Test_data)
print("test_data = ", np.asarray(Test_labels).shape, "\t", np.asarray(Test_data).shape)


Test_dict = {"labels":Test_labels,"trials":Test_data}
Train_dict = {"labels":Train_labels,"trials":Train_data}

# Saving the .mat files
from scipy.io import savemat
savemat("train_data.mat", Train_dict)
savemat("test_data.mat", Test_dict)