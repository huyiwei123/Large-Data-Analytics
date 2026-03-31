import numpy as np

# #数组创建
# # In[42]:
# a = np.array([1, 2, 3, 4])
# print(a)
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(a)
#-----------------------------------------------------------------
# #数组索引
# # In[1]:
# a = np.array([1, 2, 3, 4, 5])
# b = np.array([[0, 1, 2, 3], [5, 6, 7, 8], [9, 10, 11, 12]])
#
# # In[2]:
# print(a[0], a[2])
#
# # In[3]:
# print(b[0, 0], b[1, 2])
#-----------------------------------------------------------------
#数组切片
# In[46]:
a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# In[47]:
print(a[0:4], a[1::2])

# In[48]:
print(b[0:2, 1:3])
#------------------------------------------------------------------
#数组迭代
# In[49]:一维数组的遍历
for i in a:
    print(i ** 2)

# In[50]:二维数组的遍历
for i in b:
    print(i)

# In[51]:全部展开后的二维数组值
for i in b.flat:
    print(i)
#---------------------------------随机函数---------------------------
#随机数组 random
# In[52]:
a = np.random.random((3, 3))
print(a)
#随机数组 randn
# In[53]:
b = np.random.randn(3,3)
print(b)

#------------------------------拼接------------------------------------
#数组拼接
# In[54]:
a = np.array([[1, 2], [3, 4]])
print(a)

# In[55]:
b = np.array([[100, 200], [300, 400]])
print(b)

# In[56]:
a107 = np.hstack((a, b))#横向拼接
print(a107)

# In[57]:
a108 = np.vstack((a, b))#纵向拼接
print(a108)

# In[58]:
a109 = np.concatenate((a, b))#指定轴向进行拼接，默认为0(0:纵向拼接)
print(a109)

# In[59]:
a110 = np.concatenate((a, b), axis=1)#横向拼接
print(a110)
#-------------------------------------------------------------------
#数组拆分
# In[60]:
c = np.arange(24).reshape(4, 6)#重新转化大小格式
print(c)

# In[61]:
cl = np.split(c, 2, 1)#将矩阵c进行分裂，
print(cl)
#----------------------------------------------------------------------
#数组运算（add(加法), subtract(减法), multiply(乘法), divide(除法)）
# In[62]:
a1 = np.arange(9).reshape(3, 3)
a2 = np.arange(9).reshape(3, 3)
a12 = np.add(a1, a2)
print(a12)

# In[63]:
a1 = np.arange(9).reshape(3, 3)
a2 = np.arange(9).reshape(3, 3)
a12 = np.subtract(a1, a2)
print(a12)

# In[64]:
a1 = np.arange(9).reshape(3, 3)
a2 = np.arange(9).reshape(3, 3)
a12 = np.multiply(a1, a2)
print(a12)

# In[65]:
a1 = np.arange(9).reshape(3, 3)
a2 = np.arange(9).reshape(3, 3)
a12 = np.divide(a1, a2)
print(a12)

#数组运算（power, log(对数计算)）
# In[66]:
a1 = np.arange(9).reshape(3, 3)
a2 = np.arange(9).reshape(3, 3)
a12 = np.power(a1, a2)
print(a12)

# In[67]:
x = np.arange(5)
print(np.log(x))
print(np.log2(x))
print(np.log10(x))

#统计分析（maximum(取最大值计算), minimum(取最小值计算)）
# In[68]:
a1 = np.arange(9).reshape(3, 3)
a2 = np.arange(9).reshape(3, 3)
a12 = np.maximum(a1, a2)
print(a12)

# In[69]:
a1 = np.arange(9).reshape(3, 3)
a2 = np.arange(9).reshape(3, 3)
a12 = np.minimum(a1, a2)
print(a12)

#其他运算（abs(绝对值), square(平方), sqrt(开方)）
# In[70]:
a = np.array([1, 2, -3, -4])
print(a)
print(np.abs(a))

# In[71]:
a = np.arange(5)
print(a)
print(np.square(a))

# In[72]:
a = np.arange(5)
print(a)
print(np.sqrt(a))

#取整（ceil, floor）
# In[73]:
a = np.array([0.1, 1, 1.2, 2, 2.3])
print(np.ceil(a))

# In[74]:
a = np.array([0.1, 1, 1.2, 2, 2.3])
print(np.floor(a))

#排序（sort(升序排序), argsort(), lexsort）
# In[75]:
x = np.arange(16, 0, -1).reshape(4, 4)
print(x)
print(np.sort(x))

# In[76]:
x = np.arange(4, 0, -1)
print(x)
print(np.argsort(x))#返回的是原数组的索引

# In[77]:
a = np.array([1, 5, 1, 4, 3, 4, 4])
b = np.array([9, 4, 0, 4, 0, 2, 1])
print(np.lexsort((b, a)))#最后一个数组作为主排序顺序，倒数第二个键用于辅助排序


##########################
#----------------------------矩阵--------------------------------------------------          矩阵           #

#矩阵创建
# In[78]:
a = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)

# In[79]:
a = np.matrix("1 2 3;4 5 6;7 8 9")
print(a)

a=np.array(range(1,10)).reshape(3,3)
print(a)

#矩阵乘法（dot, multiply）
# In[81]:
a = np.matrix("1 2;3 4")
b = np.matrix("5 6;7 8")
print(np.dot(a, b))

# In[82]:
print(np.multiply(a, b))

#矩阵的特征值与特征向量
a = np.matrix("3 2;-1 -1")
print(a)
print(np.linalg.eig(a))