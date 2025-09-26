#Function 1: Fibonacci
def fibonacci(integer):
    a = 0
    b = 1
    count = 3
    if integer == 1:
        return 0
    if integer == 2:
        return 1
    while count != integer:
        a += b
        b += a
        count += 1
        if integer % 2 == 0:
            return a
        else:
            return b


#Function 2: Prime Numbers
def is_prime (integer):
    if integer <= 1:
        return False
    for i in range (2, integer):
        if integer % i == 0:
            return False
    return True

#Function 3: Prime Factorization
def print_prime_factors(num):
    a = 1
    while num > 1 and num % a == 0:
        if num % a == 0:
            print(a,"*", end='')
        break




