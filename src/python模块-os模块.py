import os
#listdir（）返回指定目录下的文件和目录列表
myfiles = os.listdir('D:\应用程序\pycharm\project\Big Data Analytics')
for file in myfiles:
    print(file)#打印文件名

# 重命名文件或目录
os.rename("python数据类型.py", "python数据类型new.py")

# 获取当前工作目录
os.getcwd()

# 改变当前工作目录（示例：切换到上级目录）
os.chdir("F:\\《大数据分析》上课课件\\Python课件教程\\python基础")
os.getcwd()

# 创建新目录
os.mkdir("newfolder")

# 删除空目录（确保目录为空）
os.rmdir("newfolder")

# 使用 walk 遍历目录树（在目录中游走输出在目录中的文件名）
results = os.walk("D:\应用程序\pycharm\project\Big Data Analytics")
for root, dirs, files in os.walk("D:\应用程序\pycharm\project\Big Data Analytics"):
    print("当前路径:", root)
    print("子目录:", dirs)
    print("文件:", files)