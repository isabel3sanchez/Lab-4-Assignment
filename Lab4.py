#Function 1: Fibonacci
def fibonacci(integer):
    a = 0
    b = 1
    result = a + b
    count = 3

    if integer == 1:
        return 0
    if integer == 2:
        return 1

    while count != integer:
        a = b
        b = result
        result = a + b
        count += 1
    return result


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
    print(f"{num} = ", end= '')
    a = 2
    while num > 1:
        if num % a == 0 and num != 2:
            print(f"{a}", end= '')
            if num != a:
                num = num // a
                print("* ", end='')
        else:
            a += 1
    print()

            #figure out for 2




