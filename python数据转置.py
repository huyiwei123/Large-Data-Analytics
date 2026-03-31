import numpy as np
import pandas as pd


#Transpose转置函数：只能进行最简单的整体翻转操作，与.T效果相同
df1 = pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12]], index=['name','age','id'], columns=list('ABCD'))
print(df1)
print(df1.transpose())
print(df1.T)

#transpose函数多层次行列索引数据转置
multi_df1 = pd.DataFrame(np.random.randint(1, 50, (4, 4)),
    columns=pd.MultiIndex.from_product([['Beijing','Shanghai'],['Sale','Cost']]),#两个层次的列索引
    index=pd.MultiIndex.from_product([['2020','2021'],['AFirm','BFirm']]))#两个层次的行索引
print(multi_df1)#原数据
print(multi_df1.transpose())#转置后

#---------------------------------------------数组转置-------------------------------------------
#stack()函数转置：
df1 = pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12]], index=['name','age','id'], columns=list('ABCD'))
print(df1)
df1_stack = df1.stack()#stack()将 DataFrame 的“列”旋转堆叠到“行”上，把【宽表】变成【长表】
print(df1_stack)
df1_unstack=df1_stack.unstack()
print(df1_unstack)#与原数据相同，证明两个函数为相反操作

#多层数组转置
multi_df1 = pd.DataFrame(np.random.randint(1, 50, (4, 4)),
    columns=pd.MultiIndex.from_product([['Beijing','Shanghai'],['Sale','Cost']]),
    index=pd.MultiIndex.from_product([['2020','2021'],['AFirm','BFirm']]))
print(multi_df1)
multi_df1_stack1 = multi_df1.stack(level=0)#level默认为-1（最内层），最外层为0：将最外层的列索引（Beijing,Shanghai）堆叠到行索引上
print(multi_df1_stack1)

print(multi_df1_stack1.reset_index()) #后面具体介绍reset函数
multi_df1_stack2 = multi_df1_stack1.stack()#两步生成，后面介绍一步生成dataframe
print(multi_df1_stack2) #进一步把收入和成本也变成了内层行索引

multi_df1_stack3 = multi_df1.stack(level=[0,-1])#0代表最外层索引，-1代表最内层索引（一步直接生成）
print(multi_df1_stack3)

multi_df1_unstack = multi_df1.unstack(level=0) #最外层行索引年度变为列索引
print(multi_df1_unstack)

#----------------------------------数据逆透视#melt()函数--------------------------------------------------
df2 = pd.DataFrame({'姓名':['小明','小红','小刚'],'语文':[87,90,92],
    '数学':[93,95,88],'英语':[89,95,90]})
print(df2)

df2_melt = df2.melt(id_vars ={'姓名'}, value_vars ={'语文','数学',
    '英语'}, var_name='课程', value_name='成绩')
print(df2_melt)

#若数据列索引多层，col level参数
multi_df2 = df2.copy()
multi_df2.columns = pd.MultiIndex.from_arrays([['姓名', '语文', '数学', '英语'], ['Name', 'Chinese', 'Math', 'English']])
print(multi_df2)

multi_df2_melt = multi_df2.melt(id_vars=['Name'],
                                var_name='Course', value_name='Score', col_level=-1)#col_level表堆叠的列层级，-1表示最内层
print(multi_df2_melt)

#pivot()函数
df2_melt['等级']=['B','A','A','A','A','B','B','A','A']
df3=df2_melt.copy()
print(df3)
df3_pivot1=df3.pivot(index='姓名',columns='课程',values='成绩')
print(df3_pivot1)
df3_pivot2=df3.pivot(index='姓名',columns='课程',values=['成绩','等级'])
print(df3_pivot2)

#-----------------------------------------------------数据处理实例---------------------------------------
#1.数据清洗
ownership_type = pd.read_csv(r"D:\应用程序\pycharm\project\Big Data Analytics\股权性质2011-2019.csv", index_col=0)
print(ownership_type.head(10))
ownership_type = ownership_type.drop(columns=['证券简称'])
ownership_type = ownership_type.fillna(value='缺失')
print(ownership_type.head())

cname = list(ownership_type.columns)
print(cname)
cname0 = list(cname[0])
print(cname0)

column_name = [elem[13:] for elem in cname]
ownership_type.columns = column_name
print(ownership_type.head())

ownership_type.index=[i[0:6] for i in ownership_type.index]
print(ownership_type.head())
#2.数据转置
print(ownership_type.T)
ownership_type = ownership_type.stack()
print(ownership_type)
ownership_type = ownership_type.reset_index()
print(ownership_type)
ownership_type.columns=['股票代码','会计期间','股权性质']
ownership_type['股票代码']=ownership_type['股票代码'].astype('int')
print(ownership_type)


