#缺失值查看
import numpy as np
import pandas as pd


np.random.seed(0)
df1 = pd.DataFrame(np.random.randint(1,10, size=(5,3)), columns=list('abc'))
df1.iloc[2:4,0] = np.nan
df1.iloc[0,1] = np.nan
print(df1)
print(df1.isnull())#查看缺失值，True为缺失值
print(df1.notnull())#查看缺失值，False为缺失值
print(df1.info())#进行描述性分析，看每个列有无缺失值
print(df1.isnull().sum())#对每个列的缺失值个数进行累加，输出对应列的缺失值的数量

#缺失值删除
print(df1)
print(df1.dropna())#将有缺失值的行进行剔除
print(df1.dropna(axis=1))#将有缺失值的列进行剔除（不推荐）
print(df1.dropna(how='all'))#？

#缺失值填充
print(df1.fillna(value=0))#将缺失值用0来填充
print(df1.fillna(value=df1.mean()))#使用该列的平均值进行填充
print(df1.fillna(value=df1.median()))#使用该列的中位数进行填充
print(df1.ffill())
print(df1.bfill())

#-----------------------------------------------异常值处理---------------------------------------------
df2 = pd.DataFrame({'key1': [1,1,1,3,2,4,2,100,5,2,2.3,6],
'key2': [1,1,3,2,5,50,1,0.2,2,0.5,2,4]},
index=['name1','name2','name3','name4','name5','name6','name7','name8','name9','name10','name11','name12'])

#-------------------------------3Σ方法------------------------------
df3 = df2.copy()
print(df3)

col_mean = df3['key1'].mean()#计算key1列的均值
col_std = df3['key1'].std()#计算key2列的标准差
Q1 = (np.abs(df3['key1'] - col_mean) <= 3 * col_std)#核心公式（判断异常值）：中心化与3倍的方差比较
df3['key1_bool'] = Q1#创建一个新的列，用于显示异常值
print(df3)
df3.loc[df3['key1_bool'].isin([False]), 'key1'] = df3['key1'].mean()#将异常值替换为均值（最好使用中位数进行替换），loc函数为定位
print(df3)

#同理对key2进行处理
col_mean = df3['key2'].mean()
col_std = df3['key2'].std()
Q2 = (np.abs(df3['key2'] - col_mean) <= 3 * col_std)
df3['key2_bool'] = Q2
print(df3)
df3.loc[df3['key2_bool'].isin([False]), 'key2'] = df3['key2'].mean()#key2bool为false则存在异常值
print(df3)

# 异常值批量处理
df2 = pd.DataFrame({'key1': [1,1,1,3,2,4,2,100,5,2,2.3,6],
                    'key2': [1,1,3,2,5,50,1,0.2,2,0.5,2,4]},
                   index=['name1','name2','name3','name4','name5','name6','name7','name8','name9','name10','name11','name12'])

def threesigma_outlier(df, col_list, n):#3Σ处理法的函数
    """
    使用3σ原则检测并处理异常值（将异常值替换为该列均值）
    :param df: 输入DataFrame
    :param col_list: 要处理的列名列表
    :param n: 标准差倍数（通常取3）
    :return: 处理后的DataFrame
    """
    for col in col_list:                     # for循环需要缩进
        col_mean = df[col].mean()            # 取均值
        col_std = df[col].std()               # 取标准差
        sigma_test = (np.abs(df[col] - col_mean) <= n * col_std)  # 3σ检测
        col_new = str(col) + '_bool'          # 新列名（标记是否为正常值）
        df[col_new] = sigma_test               # 新增布尔列
        df.loc[df[col_new].isin([False]), col] = col_mean  # 将异常值替换为均值
    return df                                   # 返回修改后的DataFrame

# 调用函数并打印结果
result = threesigma_outlier(df2, ['key1', 'key2'], 3)  # 使用副本避免修改原始数据
print(result)

#----------------------------------------------IQR方法-----------------------------------------------------------------
#使用IQR确定异常值、极端值
df4 = pd.DataFrame({'key1': [1,1,1,3,2,4,2,100,5],
                    'key2': [1,1,3,2,5,50,1,0.2,3]},
                   index=['name1', 'name2', 'name3', 'name4',
                          'name5', 'name6', 'name7', 'name8', 'name9'])
print(df4)
q1 = df4.quantile(.25)
q3 = df4.quantile(.75)
IQR = q3 - q1
x_low = q1 - 1.5 * IQR    # 计算下限
x_top = q3 + 1.5 * IQR    # 计算上限
d_bool = np.where(df4 < x_low, True, np.where(df4 > x_top, True, False))#判断是否为异常值（嵌套判断语句）
df5 = pd.DataFrame(d_bool, index=df4.index, columns=df4.columns)#创建一个数据，内容为d_bool，标签为df4的标签
print(df5)

#---------------------------------------------------缩尾法-----------------------------------------------------------------
#缩尾法处理异常值
#原理：先按大小进行排列，再把20%以前的点替换为20%位置的点等等
df6 = pd.DataFrame({'w': [1,3,5,7,9,11,13], 'a': [2,4,6,8,10,12,14]}, index=list('abcdefg'), columns=list('wa'))
print(df6)

from scipy.stats.mstats import winsorize#导入缩尾函数
print(winsorize(df6['w'], limits=[0.2, 0.2]))#将w列进行缩尾处理
print(winsorize(df6['a'], limits=[0.2, 0.2]))#将a列进行缩尾处理

#批量缩尾数据，并将结果添加为新列
for col in df6.columns[0:]:
    win = winsorize(df6[col], limits=[0.2, 0.2])
    col_new = str(col) + '_win'
    df6[col_new] = win
print(df6)

#-------------------------------------数据去重-----------------------------------------------------------------------------

df9 = pd.DataFrame({'wang':[1,3,3],'li':[1,3,3],'zhang':[2,3,4]})#使用字典来创建数据
print(df9)

print(df9.duplicated())#从上到下判断数据中是否有重复值（两个行数据完全一样）；与之前比较是重复行为Ture，没有为False
print(df9.duplicated(subset=['wang','li']))#忽略zhang列，仅看wang和li列
print(df9.T.duplicated())#先进行转置，再进行比较重复值

print(df9.drop_duplicates())#找出重复值的同时将其删除
print(df9.drop_duplicates(subset=['wang','li']))
print(df9.drop_duplicates(subset=['wang','li'],keep='last'))
print(df9.T.drop_duplicates())
print(df9.T.drop_duplicates().T)

#----------------------------------------------数据替换--------------------------------------------------------------

#replace（）函数：将所有的旧数据替换为新数据
df9 = pd.DataFrame({'wang':[1,3,3],'li':[1,3,3],'zhang':[2,3,4]})
df10 = df9.replace(to_replace=[3], value=0)#将所有的3替换为0
print(df10)

df9['wang']=df9['wang'].replace(to_replace=[3], value=0)#只将wang列的3替换为0
print(df9)

df9['zhang']=df9['zhang'].replace([2,3,4], 0)#同理，将zhang中的所有234替换为0
print(df9)

df9['li']=df9['li'].replace([1,3,3], [0,1,1])#分别替换
print(df9)

df9['wang'] = df9['wang'].replace(1, np.nan).bfill()
print(df9)

#insert（）函数#将指定对象插入指定位置
list=[1,1,1,1,1]
list.insert(0,0)#将0插入在第0号索引
print(list)

list.insert(6,0)#同理
print(list)

list.insert(-2,0)
print(list)

list.insert(-20,0)#索引中没有-20，那么选择最左边的数进行替换
print(list)

#--------------------------------------------数据标准化-------------------------------------------------------------------
df11 = pd.DataFrame({'key1': [1,1,1,3,2,4,2,100,5],
                    'key2': [1,1,3,2,5,50,1,0.2,3]},
                   index=['name1', 'name2', 'name3', 'name4',
                          'name5', 'name6', 'name7', 'name8', 'name9'])

#Z-Score标准化
df12=df11.copy()
for col in df11.columns[0:]:
    col_mean=df11[col].mean()#计算均值
    col_std=df11[col].std()#计算标准差
    zscore=(df11[col]-col_mean)/col_std
    col_new=str(col) + '_zscore'
    df11[col_new]=zscore#加入一个新的列
print(df11)

#min-max标准化
df13=df11.copy()
for col in df13.columns[0:]:
    col_max=df13[col].max()
    col_min=df13[col].min()
    minmax=(df13[col]-col_min)/(col_max-col_min)#公式
    col_new=str(col) + '_minmax'
    df13[col_new]=minmax#创建一个新的列
print(df13)

#使用包来进行实现
from sklearn import preprocessing as pp
from sklearn.preprocessing import minmax_scale

df14=df11.copy()
for col in df14.columns[0:]:
    zscore=pp.scale(X=df14[col].values, axis=0)#尺度函数：Z-Score标准化
    col_new=str(col) + '_zscore'#创建一个新的列
    df14[col_new]=zscore
print(df14)
#可能存在不同，因为一个使用样本标准差，一个使用总体标准差

df15=df11.copy()
for col in df15.columns[0:]:
    scaled_values = minmax_scale(df15[col].values, feature_range=(0, 1))
    col_new=str(col) + '_minmax'
    df15[col_new]=scaled_values
print(df15)

