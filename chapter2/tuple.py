"""
元组
元组——不仅仅是不可变的列表
author:wanggis
"""
import collections
# 元组作为记录的作用

# 将元组当作一些字段的集合，那么数量和位置信息就变得非常重要了。
# 如果在任何的表达式里，我们在元组内对元素排序，这些元素所携带的位置信息就会丢失
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ("Tykyo", 2003, 32450, 0.66, 8014)
travelers_ids = [('USA', '3195855'), ("BRA", "CE3422567"), ("ESP", "XDA205856")]
for passport in sorted(travelers_ids):
    print("%s, %s" % passport)

for country, _ in travelers_ids:
    print(country)

# 元组拆包
# 元组拆包可以应用到任何可迭代对象，唯一的硬性要求是，被可迭代对象中的元素数量必须要跟接受这些元素的空档数一致。除非我们用*来表示忽略的元素。
latitude, longitude = lax_coordinates   # 元组拆包
print(latitude)
print(longitude)


# 不使用中间变量交换两个变量的值
a = 1
b = 2
a, b = b, a
print(a)
print(b)

# 用*运算符把一个可迭代的对象拆开作为函数的参数
# 获得20 / 8 的商和余数

print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))
quotient, remainder = divmod(*t)
print(quotient, remainder)


# 用*来处理剩下的元素, 使用*可以是我们吧注意力集中在元组的部分元素上
a, b, *rest = range(5)
print(a, b, rest)

# 在平行赋值中，*前缀只能用在一个变量名前面，但是这个变量可以出现在赋值表达式的任意位置
a, *body, c, d = range(5)
print(a, body, c, d)
*head, b, c, d = range(5)
print(head, b, c, d)


# 嵌套元组拆包
# 接受表达式的元组可以是嵌套式的， 例如（a, b, (c, d)）
# 只要这个接受元组的嵌套结构符合表达式本身的嵌套结构

metro_areas = [
    ('tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
    ("Mexico City", "IN", 20.142, (19.433333, -99.133333)),
    ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
    ("Sao Paulo", "BR", 19.649, (-23.547778, -46.635833))
]

print("{:15} | {:^9}".format("", "lat.", "long."))
fmt = "{:15} | {:^9.4f} | {:9.4f}"
for name, cc, pop, (latitude, longitude) in metro_areas:     # 我们把输入元组的最后一个元素拆包到由变量构成的元组里，这样就获取了坐标
    if longitude <= 0:   # 将城市的输出限制在西半球的城市
        print(fmt.format(name, latitude, longitude))


# 具名元组
# collections。namedtuple 是一个工厂函数，它可以用来构建一个带字段名的元组和一个有名字的类

City = collections.namedtuple("City", "name country population coordinates")    # 创建一个具名元组需要两个参数，一个是类名，另一个是类的各个字段的名字。后者可以是由数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串
tokyo = City('tokyo', 'JP', 36.933, (35.689722, 139.691667))    # 存放在对应字段里的数据要以遗传参数的形式传入到构造函数中（注意，具名元组的构造函数只接受单一的可迭代对象）

print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)

# 具名元组还有一些自己的专有属性： _fields_类属性, 类方法_make(iterable)和实例方法 _asdict()
# example
print(City._fields)     # fields属性是一个包含这个类所有字段名称的元组
latlong = collections.namedtuple("Latlong", "lat long")   # 用 _make()通过接受一个可迭代对象来生成这个类的一个实例， 他的作用跟City(*delhi_data)是一样的
delhi_data = ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())  # _asdict()把具名元组以collections.OrderedDict 的形式返回，我们可以利用它来把元组的信息友好地呈现出来。
for key, value in delhi._asdict().items():
    print(key + ':', value)



# 元组的第二个角色：充当不可变的列表
# 除了跟增减元素相关的方法之外，元组支持列表的其他所有方法。
tuples = (1, 2, 3)
a[0] = 4      # 这句话是会报错的