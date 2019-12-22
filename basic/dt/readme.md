## 决策树(Decision Tree)
我们将讨论可以用于**分类**和**回归**任务的简单、非线性的模型 **决策树**。个人认为决策树相对于其他机器学习模型更容易理解，符合我们人类思考和对事物进行分类判断的逻辑。我们在现实生活中就是这样一步一步做出决策的。例如找对象、找工作都会不自觉用到决策树算法来做出决定我们的决定。有人可能认为现在是深度学习的天下，决策树是不是已经过时了没有立足之地了。虽然在某些应用已经打上深度神经网的标签，但是在一些领域中可能更适合选择决策树而非深度神经网模型。
### 重要性
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

#### 参考资料
> Tom Mitchell machine learning McGraw Hill.

### 什么是决策树
#### 决策树结构
决策树是由节点和分支组成，节点根据作用和位置分为根节点、节点和叶节点,叶节点给出了最后的判断。
- 根节点(root node)
- 分支(branch)
- 节点(node)
- 叶节点(leaf)
### 如何构建决策树
#### 我们来看一颗决策树
$$ outlook \Rightarrow \begin{cases}
    sunny \Rightarrow Humidity \begin{cases}
        High \Rightarrow No \\
        Normal \Rightarrow Yes
    \end{cases} \\
    overcast \Rightarrow Yes \\
    rain \Rightarrow Wind \begin{cases}
        Strong \Rightarrow No \\
        Weak \Rightarrow Yes
    \end{cases}
\end{cases}$$
这里我在 markdown 还不知道如何绘制一个树，所以暂时将树旋转了 90 来表示这个树
| Day  | Outlook  | Temperature | Humidity | Wind | PlayTennis
|---|---|---|---|---|---|
| D1  | Sunny  | Hot | High | Weak | No |
我们通过第一条数据输入到上面决策树，看一看是否给出正确的判断。
- outlook 节点 sunny
- Humidity 节点 High
- 结果 No 也就是决策树给出正确的推测

$$ outlook \Rightarrow \begin{cases}
    sunny \Rightarrow Humidity \begin{cases}
        High \Rightarrow No \\
    \end{cases} \\
    \end{cases}$$
#### 不纯度(Impurity)
其实决策树每一个节点都在做对数据纯度的改良，如果数据中不同类别数据越均匀这个数据纯度就越低，我们决策过程就是一个提纯过程，尽量让每一个叶节点都是一类数据。
#### 信息论(information theory)
在我们生活工作中充满信息，那么我们是如何度量信息大小？
C.shannon 最早研究信道通讯，后来提出信息论，因为信息论作为通信基础，有了通信才有了广播、电视和电话这些通信设备。
$$ \underbrace{01011}_{input} \rightarrow \underbrace{01011}_{output} $$

我们生活的确有很多信息，X 表示要表达的信息。如何衡量信息量，如何用数字定量表示信息大小?
$$H(X)?$$
如何比较两个信息量的大小
$$H(X_1) > H(X_2)$$
我们先从两个事件来看
1. 今天太阳从东方升起(A 事件)
2. 今天接收到了一份机器学习岗位的 offer 的邮件(B 事件)

第 1 条信息量我们听了会不以为然，因为每天太阳都会从东方升起，而第 2 条信息是让我们惊喜的，也就是这个信息给我们带来信息量比较大。我们再从概率角度考虑这两件事，太阳从东方升起是大概率事件而收到了一份机器学习岗位的 offer 是让我们有意外又惊喜的小概率事件。
$$ H(A) < H(B)$$


$$\begin{cases}
    H(X) \Leftrightarrow  \frac{1}{P(X)}  \\
    H(X_1,X_2) \Leftrightarrow H(X_1) + H(X_2) \\
    H(X) \ge 0 
\end{cases}$$
通过上面示例总结信息量有以下
1. 信息量与概率成反比
2. 独立事件的信息量可以相加
3. 信息量是大于等于 0 

为了满足上面上个条件我们可以构造这样一个函数，这个函数可以同时满足上面信息量这些特点

$$H(X) = \log \frac{1}{P(X)}$$
1. 因为 log 函数是单调递增所以满足第一条件
$$\begin{aligned}
    H(X_1,X_2) = \log \frac{1}{P(X_1)P(X_2)} \\
    = - \log(P(X_1)P(X_2)) \\
    = - \log(P(X_1) + \log P(X_2))
\end{aligned}$$
2. 这样满足了独立事件的信息量可以相加，不独立事件我们随后介绍通过条件熵来解决
信息量函数
$$H(X) = -\log P(X)$$

#### 信息熵(Entropy)
$$E_x[H(X)] = -\sum_{x} P(X) \log P(X)$$
- $E_x$ 是数学期望

$$\begin{aligned}
    E_x[f(x)] = \sum_xP(x)f(x)
    = \int_x p(x)f(x)dx
\end{aligned}$$
这是我们学过期望公式中 f(x)换成 H(x)即可,那么信息熵代表信息量函数的数学期望。
封闭物理系统，熵是不断增大，在没有和外界进行能量交换情况下整个系统从有序状态变为无序的状态。

分叉点，分类，不同类别数据交界的地方。

- 第一种情况两种数据均匀分布
$$entropy(X) =  - \frac{1}{2} \log \frac{1}{2} - \frac{1}{2} \log \frac{1}{2} = 1 \tag{original}$$
- 第二种情况只有一种类型分类(A1 事件)
$$entrop(A_1) = 0 $$
- 第三种情况是两种数据非均匀分布
$$entrop(A_2) = -\frac{2}{7} \log \frac{2}{7} - \frac{5}{7} \log \frac{5}{7} = 0.86$$
#### 信息增益(IG)
信息增加=整个信息熵-$\sum_i w_i Entropy(A_i)$
我们有$C_11^2$ 组合进行选择分割点，webb 发现一个我们只关心不同数据间分隔处。
![屏幕快照 2019-12-21 上午6.25.59.png](https://upload-images.jianshu.io/upload_images/8207483-8c18fc176d54d5e1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
我们通过切割面将高维空间混合数据进行分割，
(图)
![屏幕快照 2019-12-21 上午6.27.58.png](https://upload-images.jianshu.io/upload_images/8207483-671dd28630c50e4a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
$$entropy(X) =  - \frac{1}{2} \log \frac{1}{2} - \frac{1}{2} \log \frac{1}{2} = 1 \tag{original}$$
- 采用 A 作为分隔线
$$\begin{cases}
    entropy(A^{left}) = 0 \\
    entropy(A^{right}) = -\frac{2}{7} \log \frac{2}{7} - \frac{5}{7} \log \frac{5}{7} = 0.86
\end{cases}$$

$$entropy(A) = \frac{3}{10} \times 0 + \frac{7}{10} \times 0.86 = 0.62 $$

$$IG = 1 - 0.62 = 0.38$$

- 采用 B 作为分隔线
$$\begin{cases}
    entropy(B^{left}) = 1 \\
    entropy(B^{right}) = 1
\end{cases}$$
$$IG = 1 - 1 \times 0.6 + 1 \times 0.4 = 0$$
也就是说明B 分割线没有效果。

那么我们有了信息增益，信息增益是通过原始信息量减去分割后每一个小块信息量加权取和。信息增益越大说明分割效果最好，有关 C 情况大家可以自己试一试结果给大家
$$IG(A) > IG(C) > IG(B)$$

(图)

#### 构建 hello world 决策树
我们选择第一个根节点方法是找到 4 个特征可将通过此分类后信息增益最大。
$$\begin{cases}
    s = [9_{yes},5_{no}] \\
    S_{weak} = [6_{yes},2_{no}] \\
    S_{strong} = [3_{yes},3_{no}] \\
\end{cases}$$

$$ IG = 0.048 $$

| features  | GI  |
|---|---|
|  Outlook | 0.246  |
|  Humidity | 0.151  |
|  Wind | 0.048  |
|  Temperature | 0.029  |
以上都是 ID3 的算法

过拟合问题在决策树表现非常明显，因为我们可以通过不断分割将每一个数据划分为一个小块。例如我们按数据 id 进行分隔就是一种过拟合。
#### 特征的类型
我们根据特征类型来选择模型，简单介绍特征类型
- 离散类型
- 连续类型


### GINI
$$GINI = 1 - \sum_j [p(j|t)]^2$$

| 分类  | 数量  |
|---|---|
| c1  | 0  |
| c1  | 6  |

$$GINI = 1 - (0^2 + 1^2) = 0$$

| 分类  | 数量  |
|---|---|
| c1  | 3  |
| c1  | 3  |

$$GINI = 1 - ((\frac{1}{2})^2 + (\frac{1}{2})^2) = 0.5$$


| 分类  | 数量  |
|---|---|
| c1  | 2  |
| c1  | 4  |

$$GINI = 1 - ((\frac{1}{3})^2 + (\frac{2}{3})^2) = 0.44$$

通过观察上面不同分类
指导整个数据分类，
$$GINI_{split} = \sum_{i=1}^k \frac{n_i}{n} GINI(i)$$
看起来有点像信息增益，GINI 也是越小越好,和之前信息增益取法正好相反。

这也是一种度量方式
$$Error(t) = 1 - max_{i} p(i|t)$$

![屏幕快照 2019-12-21 上午8.17.11.png](https://upload-images.jianshu.io/upload_images/8207483-1972b509dcae90e5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

树越来越深，我们需要什么时候停止，如果树越来越深可能出现过拟合，集成学习，我们只需要延伸一点就可以。我们在实际开发中很少用一个决策树来解决实际问题，因为决策树是弱分类器。

如何把误差