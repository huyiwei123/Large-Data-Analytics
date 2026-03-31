#数据的基本属性
import numpy as np
import pandas as pd
# from pandas.conftest import axis

nd=np.array([[3,5,8,0],[2,5,9,1],[1,4,7,2]])
df1=pd.DataFrame(nd,index=['code1','code2','code3'], columns=['n1','n2','n3','n4'])
print(df1)

index=df1.index
print(index)
column=df1.columns
print(column)

value=df1.values
print(value)#输出np数组

#数据的结构属性
nd=np.array([[3,5,8,0],[2,5,9,1],[1,4,7,2]])
df1=pd.DataFrame(nd,index=['code1','code2','code3'], columns=['n1','n2','n3','n4'])
print(df1)

print(df1.shape)
values=df1.values
print(values.shape)#(3,4)
print(df1.shape[0])
print(df1.shape[1])
print(df1.size)

#数据序列提取
nd = np.array([[3,5,8,0],[2,5,9,1],[1,4,7,2]])
df1 = pd.DataFrame(nd, index=['code1','code2','code3'], columns=['n1','n2','n3','n4'])
nd1 = df1['n3']
print(nd1)
print(df1['n1'])
print(df1[['n1','n3']])
print(df1[['n3']].index)
print(df1['n3'].dtype)
print(df1['n3'].values)

#--------------------------------------------------------------------
#查看数据基本信息
nd = np.array([[3,5,8,0],[2,5,9,1],[1,4,7,2]])
df1 = pd.DataFrame(nd, index=['code1','code2','code3'], columns=['n1','n2','n3','n4'])
print(df1.info())#查看数据的基本信息
#数据基本描述
print(df1.describe())#输出最小、最大、各分位数
print(df1.describe(percentiles=[0.2,0.4,0.6,0.8]))#输出分位数

#读取数据前后几行
print(df1.head(2))#输出前两行
print(df1.tail(1))
print(df1.tail())
print(df1.head(-1))
#数据分位数
print(df1.quantile([0.5]))

#数据标签重命名
l = [1,2,3,4],[5,6,7,8],[9,10,11,12]
df2 = pd.DataFrame(l, index=['name1','name2','name3'], columns=list('abcd'))
print(df2)

df2.columns = list('ABCD')
print(df2)
df2.index = ['name','age','id']#改变行索引为自己想要的
print(df2)
df3 = df2.rename(columns={'C':'X','D':'Y'})#重命名列标名称
print(df3)
df4 = df2.rename({'C':'X','D':'Y'},axis=1)#同上,axis=0为行索引
print(df4)

#-------------------------------------------------------------------------------
#数据抽样
nd2 = np.array([[3,5,8,0],[2,5,9,1],[1,4,7,2],
    [0,4,3,8],[5,5,8,9],[1,2,3,4]])

df5 = pd.DataFrame(nd2, columns=['n1','n2','n3','n4'],
    index=['code1','code2','code3','code4','code5','code6'])

print(df5)
print(df5.sample())
print(df5.sample(n=5))#随机选取n行数据
print(df5.sample(frac=0.5))#选取一定比列的数据

#数据唯一值统计
se = pd.Series([1,3,4,5,2,2,3])
print(se.unique())#统计一维数组的不同值
df6 = pd.DataFrame({'A': [1, 2, 3], 'B': [1, 2, 1]})
print(df6.nunique())#返回不同值的个数

#数据简单计算值
df6 = pd.DataFrame({'A': [1, 2, 3], 'B': [1, 2, 1]})
print(df6)
print(df6.sum())
print(df6.mean())
print(df6.min())
print(df6.max())
print(df6.count())
print(df6.median())
print(df6.std())
print(df6.corr())