num = 23
running = True
while running:
    guess= int(input('请输入一个整数：'))
    if guess == num:
        print('答对了')
        running = False
    elif guess < num:
        print('猜小了')
    else :
        print('猜大了')
else:print('结束')