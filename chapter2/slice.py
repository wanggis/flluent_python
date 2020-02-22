"""
切片
切片操作比人们想想的要强大很多
author:wanggis
"""

# 本节主要是讨论这些高级切片形式的用法，其内部的实现方法会在chapter10 提到


# 为什么切片和区间会忽略最后一个元素
# 因为这一习惯符合python， C和其他语言里一0作为起始下标的传统
# 有如下优点：
# 当只有最后一个位置信息时， 我们也可以快速看出切片和区间里有几个元素：range(3) 和my_list[:3] 都返回3个元素

l = [10, 20, 30, 40, 50, 60]
print(l[:2])

print(l[2:])


# 对对象进行切片操作
# 可以使用s[a:b:c]的形式对s在a和b之间以c为间隔取值，c的值还可以为负， 负值意味着反向取值
# a,b,c这种用法只能作为索引或者下标用在[]中来返回一个切片对象：slice(a,b,c)
# 对 seq[start:stop:step]进行求值时,python会调用seq.__getitem__(slice(start, stop, step)),详见chapter10
s = "bicyle"
print(s[::3])
print(s[::-1])
print(s[::-2])


# 进一步理解切片对象slice
invoice = """
0.....6.................................40........52...55........
1909  Pimoromi PiBrella                     $17.50    3    $52.50
1489  6mm Tactile Switch *20                 $4.95    2     $9.90
1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
1601  PiTFT Mini Kit 320*240                $34.95    1    $34.95
"""
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]   # 细节
for item in line_items:
    print(item[QUANTITY], item[DESCRIPTION])


# 多维切片和省略
# [] 运算符里还可以使用以逗号分开的多个索引或者是切片
# 要正确处理这种[]运算符的话，对象的特殊方法__getitem__ 和__setitem__ 需要以元组的形式来接受a[i, j]中的索引。
# 也就是说，如果要得到a[i, j]的值，Python会调用a.__getitem__((i,j))
# 暂时就先不写这部分了，有点搞不清楚。。。


# 给切片赋值
# 如果把切片放在赋值语句的左边，或者把他作为del的操作对象，我们就可以对序列进行嫁接、切除或就地修改操作。
l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)
l[3::2] = [11, 22]
print(l)
l[2:5] = [100]
print(l)
l[2:5] = 100     # 如果赋值的对象是一个切片，那么赋值语句的右侧必须是一个可迭代对象。即便只有单独一个值， 也要吧塔转换成可迭代的序列
