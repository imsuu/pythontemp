'''
#记得 冒号： ！！！！！！！！！！！！！！！！！！！！！！！！！
#if else
number = 23
guess = int(input('Enter an integer : '))
if guess == number:
    # 新块从这里开始
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # 新块在这里结束
elif guess < number:
    # 另一代码块
    print('No, it is a little higher than that')
    # 你可以在此做任何你希望在该代码块内进行的事情
else:
    print('No, it is a little lower than that')
# 你必须通过猜测一个大于（>）设置数的数字来到达这里。
print('Done')

#while
number=23
running=True
while running:
    guess = int(input('Enter'))
    if guess == number:
        print('Congratulation')
        running = False
    elif guess < number:
        print('NO,<')
    else:
        print('No,>')
else:
    print('nothing')
print('Done')

#for
for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')

#break
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')
'''
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')
