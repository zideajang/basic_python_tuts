import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from matplotlib.colors import ListedColormap
cmap = ListedColormap(['#FF0000','#00FF00','#0000FF'])

iris = datasets.load_iris()
X,y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=1234)

# print(X_train.shape)
# print(X_train[0])

# print(y_train.shape)
# print(y_train)

# plt.figure()
# plt.scatter(X[:,0],X[:,1],c=y,cmap=cmap,edgecolors='k',s=20)
# plt.show()

# a = [1,1,1,3,5,6,7,7,8]
# from collections import Counter
# most_common = Counter(a).most_common(1)
# print(most_common)

from knn_model import KNN
clf = KNN(k=3)
clf.fit(X_train,y_train)
predictions = clf.predict(X_test)

acc = np.sum(predictions == y_test) / len(y_test)
print(acc)