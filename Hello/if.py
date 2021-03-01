num = 23
guess = int(input('请输入一个整数'))
if guess == num:
    print('恭喜你答对了')
elif guess < num:
    print('还要再大一点')
else :
    print('还要再小一点')
print('结束')