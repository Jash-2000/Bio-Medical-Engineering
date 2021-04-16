import numpy as np
from sklearn.tree import DecisionTreeRegressor 

X_train = np.load('../asset/x_train.npy')
X_test = np.load('../asset/x_test.npy')
y_train = np.load('../asset/y_train.npy')
y_test = np.load('../asset/y_test.npy')


eeg_model = DecisionTreeRegressor(random_state=1)
eeg_model.fit(X_train,y_train)
eeg_model_result = eeg_model.predict(X_test)
print("Predictions:")
print(eeg_model_result)
print("Actuals:")
print(y_test)

new = y_test - eeg_model_result
count = 0
for i in new:
	if(i == 0):
		count = count + 1

print("\n\n Accuracy is : ", count/len(y_test))


