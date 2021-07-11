"""
Created on 08/07/21 19:46:46
@author: Jash Shah
"""
import pandas as pd
import scipy.io as io
import numpy as np
import functools
import random
import pandas as pd

def uppertri(C):
    """
    Function for extracting 1-D vector out of covariance matrix.
    """    
    uppertrain = np.asarray([1.0] * int(len(C) * (len(C) - 1) / 2))
    x = 0
    for i in range(len(C)):
        for j in range(i + 1, len(C)):
            uppertrain[x] = C[i][j]
            x += 1
    return uppertrain


def csp_func(C_a, C_b, n):
    """
    Function for calculating CSP coefficients.
    """
    C = C_a + C_b
    rtol = 1e-15
    e, E = np.linalg.eigh(C)
    P = functools.reduce(np.dot,
       [E, np.diag(np.where(e > np.max(e) * rtol, e, np.inf) ** -.5), E.T])
    
    P_C_b = functools.reduce(np.dot, [P, C_b, P.T])
    _, _, B = np.linalg.svd((P_C_b))
    W = np.asarray(np.dot(B, P.T))
   
    assert W.shape[1] >= n
    #outer = np.roll(int(np.arange(n) - n / 2), int((n + 1) / 2))
    coffs = np.asarray([W[i] for i in range(n)])
    return coffs


def filt(X,coffs):
    dotproduct = np.asarray([np.dot(coffs, trial) for trial in X])
    cov_mat = np.var(dotproduct, axis=2)
    return cov_mat


"""
Loading the train data train_mat variable. 
This includes trials and labels into X and Y
"""

train_mat = io.loadmat("C:/Users/bhargav Pandya/Desktop/BCI_Assignment/Assignment_2k21/assignment_train_data.mat")
test_mat = io.loadmat("C:/Users/bhargav Pandya/Desktop/BCI_Assignment/Assignment_2k21/assignment_test_data.mat")
x_test = test_mat['trials']
x_train = train_mat['trials']
labels_train = train_mat['labels']
print("Training Dataset contains : ",x_train.shape[0])
print("Testing Dataset contains : ",x_test.shape[0])


Y_test = []
df=pd.read_csv('C:/Users/bhargav Pandya/Desktop/BCI_Assignment/Assignment_2k21/Solution/true_test_labels.csv', sep=',')
arr = df.to_numpy()
for i in arr:
    Y_test.append(i[1])
Y_test = np.array(Y_test)
Y_train = np.asarray( np.asmatrix(labels_train).transpose())

"""
 Compute co-variance matrix for all trials
"""

X_train = np.asarray([ np.cov(x) for x in x_train])
X_test = np.asarray([ np.cov(x) for x in x_test])


"""
 Next segement of code is implementation of actual CSP Algorithm.
 
 CSP require average covarience matrix for class A (left hand) and class B (right hand)
"""

cov_X_A =  X_train[np.asarray( [True if Y_train[i]==1  else False for i in range(len(Y_train))])] 
cov_X_B =  X_train[np.asarray( [False if Y_train[i]==1  else True for i in range(len(Y_train))])] 

"""
# Calculate average covariance (Ca, Cb) matrices
"""

avg_cov_A = cov_X_A[0]
for i in range(1,len(cov_X_A)):
    avg_cov_A+=cov_X_A[i]
avg_cov_A = avg_cov_A/len(cov_X_A)

avg_cov_B = cov_X_B[0]
for i in range(1,len(cov_X_B)):
    avg_cov_B+=cov_X_B[i]   
avg_cov_B = avg_cov_B/len(cov_X_B)

"""
# Calculate CSP filter coefficients
"""
coffs = csp_func(avg_cov_A, avg_cov_B, 3)
coffs= np.asmatrix(coffs);
cspmask = np.matmul( coffs[0].transpose(),coffs[0])



################################# Applying CSP  Filter 
X_train_csp = filt(X_train, coffs)
X_test_csp = filt(X_test, coffs)
print("The feature vector has shape of: ", X_train_csp.shape[1])

from sklearn import svm

model = svm.SVC(degree= 3, kernel='linear', C= 1.0, verbose= False, probability= True, coef0= 0.0, max_iter= -1,
                decision_function_shape='ovr', random_state= None, tol= 1.0, cache_size= 400, 
                shrinking= True, gamma='auto', class_weight= None)


"""
# Find Classification accuracy using CSP Filter
"""
model.fit(X_train_csp,Y_train.ravel())
result_test = model.score(X_test_csp, Y_test)
print("Accuracy using CSP filters: "+str(result_test))