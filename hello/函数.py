'''
#函数 函数可以通过关键字 def 来定def func():
#简单函数
def say_hello():
    # 该块属于这一函数
    print('hello world')
    # 函数结束
say_hello() # 调用函数
say_hello() # 再次调用函数

#有参数的函数
def print_max(a,b):
    if a > b:
        print(a)
    elif a == b:
        print(a)
    else:
        print(b)

print_max(3, 4)

x = 5
y = 7
print_max(x,y)

#局部变量
x = 50
def func(x):
    print('x is', x)
    x = 2
    print('changed x',x)

func(x)
print('x is still',x)

#global
x = 50
def func():
    global x
    print('x is', x)
    x = 2
    print('Changed global x to', x)
func()
print('Value of x is', x)

#默认参数值  def func(a, b=5) 是有效的，但 def func(a=5, b) 是无效的。
def say(message,time=1):
    print(message*time)
say('hello')
say('as',2)

#关键字参数  命名——即关键字参数——指定
def key_word(a,b=2,c=3):
    print('a is ',a,'b is',b,'c is',c)
key_word(1)
key_word(1,3)
key_word(25,c=5)
key_word(c=10,a=5)

def print_max(a,b):
    if a > b:
        print(a)
    elif a == b:
        print(a)
    else:
        print(b)
print_max(3, 4)
print_max(b=1,a=4)

#可变参数**************************************************
def total(a=5, *numbers, **phonebook):
    print('a', a)
    #遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)
    #遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
total(10,1,2,3,Jack=1123,John=2231,Inge=1560)

#return 语句
def maxinum(x,y):
    if x>y:
        return x
    elif x==y:
        return 'the nums are equal'
    else:
        return y
print(maxinum(3,4))

# pass 语句用于指示一个没有内容的语句块
def some_function():
    pass
'''
#该文档字符串所约定的是一串多行字符串，其中第一行以某一大写字母开始，以句号结束。第二行为空行，后跟的第三行开始是任何详细的解释说明
def print_max(x, y):
    '''Prints the maximum of two numbers.打印两个数值中的最大数。

    The two values must be integers.这两个数都应该是整数'''
    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')
print_max(3, 5)
print(print_max.__doc__)

'''如果你曾使用过 Python 的 help() 函数，那么你应该已经了解了文档字符串的用途了。它所
做的便是获取函数的 __doc__ 属性并以一种整洁的方式将其呈现给你。你可以在上方的函数
中尝试一下——只需在程序中包含 help(print_max) 就行了。要记住你可以通过按下 q 键
来退出 help 。
自动化工具可以以这种方式检索你的程序中的文档。因此，我强烈推荐你为你编写的所有重
要的函数配以文档字符串。你的 Python 发行版中附带的 pydoc 命令与 help() 使用文档字
符串的方式类似。'''

