num = 1248 
def countDigits(n):
    sum = 0
    while n > 0:
        r = n % 10
        sum += r
        n = n // 10
        
    return sum
print(countDigits(num))



