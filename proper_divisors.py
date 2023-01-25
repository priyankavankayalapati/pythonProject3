def helloPerfect(num):
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    print(sum_divisors)
helloPerfect(57)