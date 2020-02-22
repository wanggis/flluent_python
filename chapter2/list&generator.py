"""
列表推导和生成器表达式
python 也从ABC那里继承了用统一的风格去处理序列数据类型
author：wanggis
"""
import array
# 列表推导是快速构建列表(list)的快捷方式（这是其唯一的作用，原书），而生成器表达式则可以用来创建其他任何类型的序列
# 列表推导的作用是为了让代码变得更加简洁，切记不可以乱用

symbols = "$¥€£¢¤"
codes = []
# 传统方法将字符串变成unicode码位的列表

for symbol in symbols:
    codes.append(ord(symbol))
print("传统方法:", codes)

# 利用列表推导的方法进行转换

codes = [ord(symbol) for symbol in symbols]

print("列表推导:", codes)


# python3 的改进：列表推导不会再出现变量泄露的问题
x = "ABC"
dummy = [ord(x) for x in x]
# 输出的仍然是“ABC”，同时列表推导也创建了正确的列表
print(x)
print(dummy)


# 列表推导同filter和map的比较
# 会另附两者的速度比较的代码  详见list_comp_speed.py
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print("列表推导的方法：", beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print("filter/map 的方法：", beyond_ascii)

# 使用列表推导计算笛卡尔积
# 生成不同颜色，尺寸的衣服

colors = ["black", "white"]
sizes = ['S', 'M', 'L']
clothes = [(color, size) for color in colors
                         for size in sizes]
print(clothes)


# 生成器表达式

# 虽然可以用列表推导的方式来初始化元组、数组或者其他的序列类型，但是生成器表达式才是更好的选择
# 生成器表达式背后遵循了迭代器协议，可以逐个地产出元素，而不是先建立一个完整的列表，然后再把这个列表传递到某个构造函数里
# 优点：能够进一步的节省内存
# 语法和列表生成器类似,只是将方括号变成了圆括号


# 用生成器表达式初始化元组和数组

print(tuple(ord(symbol) for symbol in symbols))   # 元组

print(array.array("I", (ord(symbol) for symbol in symbols)))    # 数组


# 使用生成器表达式计算笛卡尔积

for tshirt in ("%s %s" % (c, s) for c in colors for s in sizes):
    print(tshirt)
