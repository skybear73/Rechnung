import matplotlib.pyplot as plt
from sklearn import svm
X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y) 

clf.predict([[2., 2.]])

# get support vectors
clf.support_vectors_


# get indices of support vectors
clf.support_ 

# get number of support vectors for each class
clf.n_support_ 

X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
clf = svm.SVC(decision_function_shape='ovo')
clf.fit(X, Y) 




dec = clf.decision_function([[1]])
dec.shape[1] # 4 classes: 4*3/2 = 6

clf.decision_function_shape = "ovr"
dec = clf.decision_function([[1]])
dec.shape[1] # 4 classes

print(dec)

dec.plot()
plt.show()