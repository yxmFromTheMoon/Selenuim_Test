# ASCIIb编码，表示英语及西欧语言，占8bit/1bytes
# Unicode,国际标准，2bytes，好处：字符与数字之间转换速度更快一些，坏处：占用空间大
# GBK 中文字符集，支持繁体 2bytes
# UFT-8 精准，对不同的字符用不同的长度表示，好处：节省空间，缺点：速度慢，需要计算
a = 'hello world'
b = 'I like Python'
# print(type(a))
# a1 = a.encode()
# print(a1)
# print(a+b)
# print(a*10)

print(a[0])
print(a[-1])

# 切片,左闭右开[)
# print(a[1:3])
# print(a[3:])  # 3之后的所有字符.包括3
# print(a[:7])  # 7之前所有的字符，不包括7
# print(a[-1:])  # 从后往前切
print(a[-1:-5:-1])


# 不写步长，默认为1，绝对值大小决定切取的间隔，正负号决定方向，正数从左往右，负数从右往左

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def say_hello(cls):
        print(cls.name)

    def __new__(cls, *args, **kwargs):
        pass
