def fibonacci(n):
    if n <= 0:
        return n
    elif n == 1 :
        return n
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))
