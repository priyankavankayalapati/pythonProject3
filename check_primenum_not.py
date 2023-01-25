"if max_num % i == 0 " " % "
def checkPrime(max_num):
    if max_num <= 1:
        return False
    for i in range(2, max_num):