import scipy.io as sc
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler

feature = sc.loadmat("C:/Users/Jash Shah/Desktop/data.mat") # Dictionary named loader created. 
loader = feature['S1_nolabel6']            # Converted to numpy array

i = 1
cols = []
while i<65:
    colName = "Electrode" + str(i)
    cols.append(colName)
    i = i+1
cols.append("Label")

df = pd.DataFrame(loader, columns = cols)

# Printing the dataframe
print("\n\n Printing the Original Dataframe")
print(df.head())
# Printing the count of each label
print("\n\n Printing the count of each label")
print(df["Label"].value_counts())
# Using countplots
print("\n\n The countplot is as follows")
sns.countplot(x="Label", data=df)


x=df.drop(["Label"]  ,axis=1)
print("\n\n Printing the shape of x")
print(x.shape)
scaler = StandardScaler()
scaler.fit(x)
x = scaler.transform(x)

y = df.loc[:,"Label"].values
print("\n\n Printing the shape of y")
print(y.shape)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 4)

# Now saving these files.
np.save('../asset/x_train.npy', x_train)
np.save('../asset/x_test.npy', x_test)
np.save('../asset/y_train.npy', y_train)
np.save('../asset/y_test.npy', y_test)