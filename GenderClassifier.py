from sklearn import tree

# [height, weight, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40]]
# [gender]
Y = ['male', 'male', 'female', 'female', 'male']
# Decision Tree Classifier
clf = tree.DecisionTreeClassifier()
# Fit the data
clf = clf.fit(X, Y)
# Predict
prediction = clf.predict([[150, 60, 30]])

print(prediction)


