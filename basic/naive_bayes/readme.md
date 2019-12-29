### Naive Bayes(朴素贝叶斯)

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$
这就是贝叶斯概率，我们知道贝叶斯概率是由条件概率和全概率推导出来
$$ \underbrace{P(A|B)}_{postierior} = \frac{\underbrace{P(B|A)}_{likelihood}\underbrace{P(A)}_{prior}}{P(B)}$$

- posterior 是后验概率
- prior 是先验概率
- likelihood 是似然

我们现有样本数据
$$D = {(x^{(1)},y^{(1)}),(x^{(2)},y^{(2)}),\dots,(x^{(N)},y^{(N)})}, x \in \mathbb{R}^n$$
我们数据中每个样本 x 是有 n 个维（特征)向量，也是就是存在高维空间。
$$p(y|x_1,x_2,\dots,x_n) = \frac{p(x_1,x_2,\dots,x_n|y)p(y)}{p(x_1,x_2,\dots,x_n)}$$



$$
\begin{aligned}
    p(x_1,x_2,\dots,x_n) = p(x_1)p(x_2)\dots p(x_n) \\
    p(x_1,x_2,\dots,x_n|c) = p(x_1|c)p(x_2|c)\dots p(x_n|c)
\end{aligned}
$$

假设样本的特征是相互独立
$$p(x_1,x_2,\dots,x_n|y) = \prod_{i=1}^n p(x_i|y)$$

我们这里简化一下问题，我们这里有两个类别，分别$c_1$ 和 $c_2$
$$C=\{c_1,c_2\}$$
这里x 属于 $c_1$ 或是 $c_2$ 的概率和为 1
$$p(c_1|x) + p(c_2|x) = 1$$
$$\begin{aligned}
    = \frac{p(x|c)p(c)}{\sum_j p(x|c_j)p(c_j)}
\end{aligned}$$

$$p(c_1|x) = \frac{p(x|c_1)p(c_1)}{p(x|c_1)p(c_1) + p(x|c_2)p(c_2)}$$

这里分母的作用是起到正则化作用，$p(c_1)$ 是先验概率也可以忽略不计

$$p(c|x) \varpropto \prod_{i=1}^n (p(x_1|c)p(c)) $$

| Day  | Outlook  | Temperature | Humidity | Wind | PlayTennis
|---|---|---|---|---|---|
| D1  | Sunny  | Hot | High | Weak | No |
| D2  | Sunny  | Hot | High | Strong | No |
| D3  | Overcast  | Hot | High | Weak | Yes |
| D4  | Rain  | Mild | High | Weak | Yes |
| D5  | Rain  | Cool | Normal | Weak | Yes |
| D6  | Rain  | Cool | Normal | Strong | No |
| D7  | Overcast  | Cool | Normal | Strong | Yes |
| D8  | Sunny  | Mild | High | Weak | No |
| D9  | Sunny  | Cool | Normal | Weak | Yes |
| D10  | Rain  | Mild | Normal | Weak | Yes |
| D11  | Sunny  | Mild | Normal | Strong | Yes |
| D12  | Overcast  | Mild | High | Strong | Yes |
| D13  | Overcast  | Hot | Normal | Weak | Yes |
| D14  | Rain  | Mild | High | Strong | No |

$$p(yes|sunny,cool,high,strong)$$
$$p(yes|sunny,cool,high,strong) \varpropto p(sunny|yes)p(cool|yes)p(high|yes)p(strong|yes)$$

|   |   |
|---|---|
| sunny(yes)  | $\frac{}{9}$  |


```
class NaiveBayes:
    def fit(self,X,y):
        n_samples,n_features = X.shape
        # 获取类别
        self._classes = np.unique(y)
        # 获取类别总数
        n_classes = len(self._classes)
        # 对于每一个类别
        # 初始化 mean var priors
        self._mean = np.zeros((n_classes,n_features),dtype=np.float64)
        self._var = np.zeros((n_classes,n_features),dtype=np.float64)
        self._priors = np.zeros(n_classes,dtype=np.float64)

        for c in self._classes:
            X_c = X[c==y]
            self._mean[c,:] = X_c.mean(axis=0)
            self._var[c,:] = X_c.var(axis=0)
            self._priors[c] = X_c.shape[0] / float(n_samples)

    def predict(self,X):
        y_pred = [self._predict(x) for x in X]
        return y_pred

    def _predict(self,x):
        posteriors = []

        for idx,c in enumerate(self._classes):
            prior = np.log(self._priors[idx])
            class_conditional = np.sum(np.log(self._pdf(idx,x)))
            posterior = prior + class_conditional
            posteriors.append(posterior)

        return self._classes[np.argmax(posteriors)]
            # posterior 
    
    def _pdf(self,class_idx,x):
        mean = self._mean[class_idx]
        var = self._var[class_idx]
        numerator = np.exp(-(x-mean)**2/ (2*var))
        denominator = np.sqrt(2*np.pi*var)
        return numerator/denominator

```
```
# coding=utf-8
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

from nb import NaiveBayes

def accuracy(y_true,y_pred):
    accuracy = np.sum(y_true==y_pred) /len(y_true)
    return accuracy


X,y = datasets.make_classification(n_samples=1000,n_features=10,n_classes=2,random_state=123)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=123)

nb = NaiveBayes()
nb.fit(X_train,y_train)
predictions= nb.predict(X_test)

print(accuracy(y_test,predictions))
# 0.965
```