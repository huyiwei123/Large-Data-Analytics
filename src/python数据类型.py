# 数值类型基础
a = 10          # int（整型）
b = 3.14        # float（浮点型）
c = True        # bool（布尔型）
d = 3 + 4j      # complex（复数）

# 使用type()查询类型
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'bool'>
print(type(d))  # <class 'complex'>

# 浮点数指数形式
e = 7E-2    # 0.07
f = 1.5e3   # 1500.0
print(e, f)

# 单引号和双引号字符串
str1 = 'Hello Python'
str2 = "Hello Python"
print(str1)
print(str2)

# 包含引号的字符串
str3 = "I'm a student"
str4 = 'He said "Hello"'
print(str3)
print(str4)

# 长字符串（三引号）
long_str = '''I love lianghuatouzi.
please give me some support'''
print(long_str)

# 创建列表 - 方法1：直接赋值
list1 = ["ABC", 1, [2, 3], 4.2]
list2 = [1, 2, 3, 4, 5]
print(list1)
print(list2)

# 创建列表 - 方法2：使用list()函数
str_to_list = list("Hello")      # ['H', 'e', 'l', 'l', 'o']
tuple_to_list = list((1, 2, 3))  # [1, 2, 3]
print(str_to_list)
print(tuple_to_list)

# 索引访问
my_list = [10, 20, 30, 40, 50]
print(my_list[0])    # 第一个元素：10
print(my_list[-1])   # 最后一个元素：50
print(my_list[2])    # 第三个元素：30

# 切片访问
print(my_list[1:4])      # [20, 30, 40]
print(my_list[:3])       # [10, 20, 30]
print(my_list[0:4:2])      # [10, 30]（步长为2）
print(my_list[::-1])     # [50, 40, 30, 20, 10]（反转）

# 创建元组 - 方法1：使用()
tuple1 = ("ABC", 9, [4, 2, 3], 4.2)
tuple2 = (1, 2, 3, 4, 5)
print(tuple1)
print(tuple2)

# 创建元组 - 方法2：使用tuple()函数
str_to_tuple = tuple("Hello")      # ('H', 'e', 'l', 'l', 'o')
list_to_tuple = tuple([1, 2, 3])   # (1, 2, 3)
print(str_to_tuple)
print(list_to_tuple)

# 索引访问
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[0])    # 第一个元素：10
print(my_tuple[-1])   # 最后一个元素：50

# 切片访问
print(my_tuple[1:4])      # (20, 30, 40)
print(my_tuple[::2])      # (10, 30, 50)

# 注意：元组不可变
# my_tuple[0] = 100  # 这会报错！

# 创建集合 - 方法1：使用{}
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 2, 3, 3, 3}  # 自动去重，结果为 {1, 2, 3}
print(set1)
print(set2)

# 创建集合 - 方法2：使用set()函数
list_to_set = set([1, 2, 3, 3, 3])  # {1, 2, 3}
print(list_to_set)

# 集合的访问（使用for循环）
my_set = {10, 20, 30, 40, 50}
for n in my_set:
    print(n)

# 注意：集合是无序的，不支持索引和切片
# print(my_set[0])  # 这会报错！

# 创建字典 - 方法1：使用{}
dict1 = {
    "name": "张三",
    "age": 25,
    "city": "北京"
}
print(dict1)

# 键可以是整数、字符串、元组
dict2 = {
    1: "整数键",
    "key": "字符串键",
    (1, 2): "元组键"
}
print(dict2)

# 创建字典 - 方法2：使用dict()函数
dict3 = dict(name="李四", age=30, city="上海")
dict4 = dict([("a", 1), ("b", 2), ("c", 3)])
print(dict3)
print(dict4)

# 访问字典 - 方法1：键访问
print(dict1["name"])   # 张三
# print(dict1["gender"])  # 键不存在会报错！

# 访问字典 - 方法2：使用get()方法
print(dict1.get("name"))      # 张三
print(dict1.get("gender"))    # None（键不存在返回None）
print(dict1.get("gender", "未知"))  # 可以设置默认值