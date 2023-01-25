def Isperfect(num):
    reddy = 0
    for i in range(1, num):
        if num % i == 0:
            reddy += i
    if reddy == num:
        print('true')
    else:
        print('false')
Isperfect(28)