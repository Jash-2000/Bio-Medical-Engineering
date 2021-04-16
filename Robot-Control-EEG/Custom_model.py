# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import sklearn
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
from sklearn.metrics import confusion_matrix
from sklearn.metrics import multilabel_confusion_matrix

X_train = np.load('../asset/x_train.npy')
X_test = np.load('../asset/x_test.npy')
y_train = np.load('../asset/y_train.npy')
y_test = np.load('../asset/y_test.npy')

y_train = y_train.astype('float64')
y_test = y_test.astype('float64')

from keras.utils import to_categorical
y_test = to_categorical(y_test)
y_train = to_categorical(y_train)
y_test

eeg_model = Sequential()
# Input layer
eeg_model.add(Dense(32, activation='relu', kernel_initializer='random_normal', input_dim=64))
eeg_model.add(Dropout(0.25))
# First  Hidden Layer
eeg_model.add(Dense(20, activation='relu', kernel_initializer='random_normal'))
eeg_model.add(Dropout(0.5))
# Second Hidden Layer
eeg_model.add(Dense(10, activation='relu', kernel_initializer='random_normal'))
eeg_model.add(Dropout(0.5))
#Output Layer
eeg_model.add(Dense(6, activation='softmax', kernel_initializer='random_normal'))
#Compiling the neural network
eeg_model.compile(optimizer ='adam',loss='categorical_crossentropy', metrics =['accuracy'])

#Fitting the data to the training dataset
eeg_model.fit(X_train,y_train, batch_size = 10, epochs=250)
eval_eeg_model=eeg_model.evaluate(X_train, y_train)
y_pred=eeg_model.predict(X_test)

print("\n\n Predictions:")
eeg_model_result = eeg_model.predict(X_test)
print(eeg_model_result)
print("\n\n Actuals:")
print(y_test)

y_pred = []
for y in eeg_model_result:
  max = np.amax(y)
  if (max == y[1]):
    y_pred.append(1)
  elif (max == y[2]):
    y_pred.append(2)
  elif (max == y[3]):
    y_pred.append(3)
  elif (max == y[4]):
    y_pred.append(4)
  elif (max == y[5]):
    y_pred.append(5)
  else:
    y_pred.append(0)

y_real = []
for y in y_test:
  max = np.amax(y)
  if (max == y[1]):
    y_real.append(1)
  elif (max == y[2]):
    y_real.append(2)
  elif (max == y[3]):
    y_real.append(3)
  elif (max == y[4]):
    y_real.append(4)
  elif (max == y[5]):
    y_real.append(5)
  else:
    y_real.append(0)

len(y_pred)

rand = 5
choosen = np.array(X_test[rand])
electrode = []
for t in range(64):
  electrode.append(t+1)
electrode = np.array(electrode)

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(electrode, choosen)  # Plot some data on the axes.

print("\n The predicted value is : ", y_pred[rand])
print("\n The real value is : ", y_real[rand])