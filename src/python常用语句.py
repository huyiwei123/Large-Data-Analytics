# In[25]: 基本if else语句
a = 1
b = 2
if a < b:
    print("a小于b")
else:
    print("a不小于b")

# In[26]: 含多个条件的if else语句
if a < 0 and b < 3:
    a = a + 1
else:
    b = b + 1
    print(a, b)

# In[27]: 多条件if-elif-else语句
a = 1
if a == 3:
    print('a值为3')
elif a == 2:
    print('a值为2')
elif a == 1:
    print('a值为1')
else:
    print('a值不符合条件')

# In[28]: 遍历元素
num = [1, 2, 3, 4]
for i in num:
    print("当前数字: %s" % i)

# In[29]: 索引迭代
num = [1, 2, 3, 4]
for i in range(len(num)):
    print('当前数字: %s' % num[i])

# In[30]: while循环
a = 0
while a < 4:
    print('结果为:', a)
    a = a + 1
print("结束！")

# In[31]: break语句示例
a = 1
while a < 5:
    print('当前值为 :', a)
    a = a + 1
    if a == 3:
        break

# In[32]: continue语句示例
a = 1
while a < 5:
    a = a + 1
    if a == 3:
        continue
    print('当前值为 :', a)

# In[33]: pass语句示例
num = [1, 2, 3, 4]
for i in num:
    if i > 2:
        pass
    print("当前数字：%s" % i)