### PCA
#### 目标
因为 feature 间总有一定相关性，造成特征冗余，增加计算量，所以需要对特征进行优化

我们想象一个房子的描述数据，例如房屋面积，以及卧室和卫生间数量是有一定相关性。90平以上房子可能有两室一厅或三室一厅

有一个矩阵X维度(m,n) m 个采样数据，每一个数据有 n 个特征
对X去均值、标准化
求$X^TX$ 或协方差

### 中值
eigenvalues
eigenvectors

$$Var(X) = \frac{1}{n} \sum (X_i - \overline{X})^2$$


### Covariance Matrix
$$Cov(X,Y) = \frac{1}{n} \sum(X_i - \overline{X})(Y_i - \overline{Y})^T$$
$$Cov(X,X) = \frac{1}{n} \sum(X_i - \overline{X})(X_i - \overline{X})^T$$

$$A \vec{v} = \lambda \vec{v}$$