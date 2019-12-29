### 斐波那契数列
1, 1, 2, 3, 5, 8, 13, 21 
序列中每一个数字都是前两数字的和
$$ fib(n) = fib(n-1) + fib(n-2)$$
重叠子问题
问题复杂度为$O(2^n)$

![屏幕快照 2019-12-28 下午8.56.21.png](https://upload-images.jianshu.io/upload_images/8207483-0b9d8a7d76121848.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
从上图中我们明显可以看到 fib(4)

$$OPT(8) max \begin{cases}
    selected & 4 + OPT(5) \\
    not select & OPT(7)
\end{cases}$$

对公式泛化一下
$$OPT(i) = \max \begin{cases}
    selected & v_i + OPT(prev(i)) \\
    not select & OPT(i-1)
\end{cases}$$

$$\begin{aligned}
    prev(8) = 5 \\
    prev(7) = 3 \\
    prev(6) = 2 \\
    prev(2) = 0 \\
\end{aligned}$$

|  No. | prev(i)   |
|---|---|
|  1 | 0   |
|  2 | 0   |
|  3 | 0   |
|  4 | 1   |
|  5 | 0   |
|  6 | 2   |
|  7 | 3   |
|  8 | 5   |


$$\begin{cases}
    OPT(2) = \begin{cases}
        
    \end{cases}
\end{cases}$$
OPT(2) = \begin{cases}
    
\end{cases}
