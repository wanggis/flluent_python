"""
如何使用，重载，覆写python内置的特殊方法：模拟数值类型
不能让特例特殊到一开始就破坏既定规则
author：wanggis
"""

from math import hypot

# 一个简单的二维向量类

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        # 把一个对象用字符串的形式表达出来以便辨认
        # __repr__和__str__的区别在于，后者是在str()函数被使用，或者在用print函数打印一个对象时才会使用。
        # __repr__是一个更好的方法
        return "Vector(%r,%r)" % (self.x, self.y)

    def __abs__(self):
        # 返回该向量的模
        return hypot(self.x, self.y)

    def __bool__(self):
        # 默认情况下，我们自己定义的类的实例总被认为是真的，除非这个类对__bool__或者__len__函数有自己的实现
        # 如果不存在__bool__方法，那么bool（x）会尝试调用x.__len__(). 若返回0， 则bool会返回False；否则返回True
        return bool(abs(self))

    def __add__(self, other):
        # 加运算
        x = self.x+other.x
        y = self.y+other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        # 向量的标量乘法
        # 注意 a*b 和 b*a 是有一定的区别
        return Vector(self.x * scalar, self.y+scalar)


### test ###

# 向量的加减
v1 = Vector(2, 4)
v2 = Vector(2, 1)

print(v1 + v2)

# 计算向量的模
v = Vector(3, 4)
print(abs(v))


# 向量的标量乘法
print(v * 3)
print(abs(v * 3))