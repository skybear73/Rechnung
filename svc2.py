from sklearn import svm
X = [[0], [1], [2], [3]]
Y = [3, 2, 1, 0]
clf = svm.SVC()
clf.fit(X, Y)  

#clf.predict([[2., 2.]])

print(clf.predict([[0]]))