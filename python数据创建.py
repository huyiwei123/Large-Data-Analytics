import numpy as np
import pandas as pd

#dataframe列表创建
data1=[600646,600519,600887]
df1=pd.DataFrame(data=data1,index=['国新文化','贵州茅台','伊利股份'],columns=['stock'])
print(df1)
data2=[12,15,14]
df2=pd.DataFrame(list(zip(data1,data2)),index=['国新文化','贵州茅台','伊利股份'],columns=['stock','price'])
print(df2)
#zip()函数是将两个数据集进行打包,index是行索引,columns是列索引

#通过数组创建
import numpy as np
import pandas as pd
data3=np.array([[3,5,8,8],[2,5,9,1],[1,4,7,2]])
df3=pd.DataFrame(data=data3,index=['code1','code2','code3'],columns=['r1','r2','r3','r4'])
print(df3)

#通过字典创建
import numpy as np
import pandas as pd
data4= {'002422':[25.82,25.28,25.13],'600683':[4.49,5.00,4.50]}#先写好一个数据的字典，再定义行索引
df4=pd.DataFrame(data4,index=['2021-11-1','2021-11-2','2021-11-3'])
print(df4)

#通过序列创建（可以自动对齐）
import numpy as np
import pandas as pd
data5={"one":pd.Series([1,2],index=["a","b"]),
    "two":pd.Series([9,8,7],index=["a","b","c"])}
df5=pd.DataFrame(data=data5)
print(df5)

#时间序列数据创建
import numpy as np
import pandas as pd
calendar=pd.date_range(start='1/1/2021', end='1/5/2021')#日期索引，起始时间
print(calendar)
data6=np.random.randn(5,4)#服从标准正态分布
df6=pd.DataFrame(data=data6, index=calendar, columns=list('OCHL'))
print(df6)

#-----------------------------------------------获取数据-----------------------------------------------------
#’读取csv、txt文本文件
import numpy as np
import pandas as pd
data7=pd.read_csv(r'D:\应用程序\pycharm\project\Big Data Analytics\选品数据筛选.csv')
print(data7)
print(data7[['商品名称','一级类目']])
print(data7[['商品名称','一级类目']].head(10))
print(data7[['商品名称','一级类目']].head())
data8 = pd.read_csv(r'D:\应用程序\pycharm\project\Big Data Analytics\选品数据筛选.csv',sep='\t')
print(data8)

#读取excel文件
data9=pd.read_excel(r'D:\应用程序\pycharm\project\Big Data Analytics\上市银行数据.xlsx')
print(data9)
data9=pd.read_excel(r'D:\应用程序\pycharm\project\Big Data Analytics\上市银行数据.xlsx',index_col=0)#行索引为0时，不输出行索引
print(data9)

#批量读取文件
import numpy as np
import pandas as pd
import os
read_data=r'D:\应用程序\pycharm\project\Big Data Analytics'
items=os.listdir(read_data)
print(items)

#筛选csv文件，加入列表中。
datalist=[]
for name in items:
    if name.endswith(".csv"):
        datalist.append(name)
print(datalist)

# data10=pd.DataFrame()
# for name in datalist:
#     data=pd.read_csv(read_data+"\\"+name)
#     data10=data10.append(data,) #可能存在append函数在包里被去除
# print(data10)

#将所有数据拼接到一起
dflist=[]
for firm in datalist:
    data= pd.read_csv(read_data+'\\'+firm)
    dflist.append(data)
data11=pd.concat(dflist)
print(data11)