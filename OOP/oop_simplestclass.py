'''
#通过 class 关键字可以创建一个类
class Person:
    pass # 一个空的代码块
p = Person()
print(p)
'''
#方法
class Person:
    def say_hi(self):
        print('Hello, how are you?')
p = Person()
p.say_hi()
# 前面两行同样可以写作
# Person().say_hi()
