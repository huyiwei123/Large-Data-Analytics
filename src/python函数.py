#函数的定义与调用
# In[34]: 定义函数 min（比较两个数的最小值）
def min(a, b):
    if a < b:
        return a
    else:
        return b

# In[35]: 调用函数 min
c = 1
d = 2
print(min(c, d))

# In[36]: 必需参数缺失示例（会引发 TypeError）
print(min())

# In[37]: 关键字参数使用示例
print(min(b=5, a=2))

# In[38]: 定义带默认参数的函数 min，并调用
def min(a, b=5):
    if a < b:
        return a
    else:
        return b

print(min(a=9, b=3))

# In[39]: 默认参数使用示例（b 使用默认值 5）
print(min(a=1))

# In[40]: 定义带可变参数的函数 printfinfo，并调用
def printfinfo(a, *b):
    print(a)
    print(b)

printfinfo(7, 8, 9, 10)



