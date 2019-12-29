from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from pca import PCA

data = datasets.load_iris()
X = data.data
y = data.target

# 150, 4
# project the data onto the 2 primary principal components

pca = PCA(2)
pca.fit(X)
X_projected = pca.transform(X)

print('shape of X:',X.shape)
print('shape of transformed X:',X_projected.shape)

x1 = X_projected[:,0]
x2 = X_projected[:,1]

plt.scatter(x1,x2,c=y,edgecolors='none',alpha=0.8,cmap=plt.cm.get_cmap('viridis',3))

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

plt.colorbar()
plt.show()