# coding=utf-8
# numpy 快
'''
5 - 00000101 binary - numpy int32 
list 内置对象 python
size
reference count
object type
object value
numpy 用更少的内存空间来存储数据，
无需检查数据类型
numpy 用contiguous memory
'''

import numpy as np
'''
# 创建数组
a = np.array([1,2,3])
print(a)
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)
# 获取数组维度
print(a.ndim)
print(b.ndim)
print(b.shape)
# 获取类型
print(a.dtype) 
# int64
a = np.array([1,2,3],dtype='int16')
print(a.dtype) 
# 获取数组元素大小（字节数)
print(a.itemsize)
print(a.size)
print(a.size * a.itemsize)
print(a.nbytes)

# 更改数据
a = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(a)
print(a.shape)
# 通过行号和列号获取数据
print(a[1,5])
print(a[1,-1])
# 获取特定行
print(a[0,:])
# 获取特定列
print(a[:,2])
# getting a litte more fancy [startindex:endindex:stepsize]
print(a[0,1:5])
print(a[0,1:-1:2])

# 更改数据
a[1,5] = 20
print(a)
a[:,2] = 5
print(a)
a[:,2] = [1,2]
print(a)

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
# 指定特定的元素
print(b[0,1,0])
print(b[:,1,:])
print(b[:,0,0])
b[:,1,:] = [[7,7],[8,8]]
print(b)

# 初始一些特定数组
print(np.zeros(5))
print(np.zeros((2,2,3)))

# all 1s matrix
print(np.ones((3,3,2)))

# any other numpy
print(np.full((2,2),6))

# any other number 

a = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(np.full_like(a,2) )

print(np.random.rand(3,2))

'''

# 中位数：中位数在一组初始数据中有个首要前提，必须进行从小到大的排列。排列后，其中间的数就是中位数。

# Random Integer values
print(np.random.randint(7,size=(3,3)))
# the identity matrix
print(np.identity(5))

arr = np.array([1,2,3])
r1 = np.repeat(arr,3)
print(r1)
# [1 1 1 2 2 2 3 3 3]
arr = np.array([[1,2,3]])
# r1 = np.repeat(arr,3,axis=0)
r1 = np.repeat(arr,3,axis=1)
print(r1)

output = np.ones((5,5))
print(output)
z = np.zeros((3,3))
z[1,1] = 9
print(z)

# output[1:4,1:4] = z
output[1:-1,1:-1] = z
print(output)

# be careful copying arrays
a = np.array([1,2,3])
b = a
print(b)
b[0] = 1000
print(a)

a = np.array([1,2,3,4,5])
print(a)
print(a+2)
print(a-2)
print(a*2)
print(a/2)
print(a**2)

# Take the sin
print(np.sin(a))

# 线性代数
a = np.ones((2,3))
print(a)
b = np.full((3,2),2)
print(b)
print(np.matmul(a,b))

c = np.identity(3)
print(np.linalg.det(c))

# 统计学
stats = np.array([[1,2,3],[4,5,6]])
print(np.min(stats))
print(np.max(stats,axis=1))
print(np.mean(stats))

# reorganizing arrays
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
after = before.reshape((1,8))
print(after)
v1 = np.vstack(before)
print(v1)