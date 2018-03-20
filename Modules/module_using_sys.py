#import 语句导入 sys 模块
'''
import sys
print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n')
'''
#直接将 argv 变量导入程序（为了避免每次都要输入 sys. ），可以通过使用 from sys import argv 语句来实现
from math import sqrt
print("Square root of 16 is", sqrt(16))
