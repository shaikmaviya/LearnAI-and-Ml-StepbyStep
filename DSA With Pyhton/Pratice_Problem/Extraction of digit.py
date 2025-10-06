n = 5783 

print(count := len(str(n)))

count = 0
num = n
while num > 0:
    digit = num % 10
    print(digit)
    num = num // 10
    count += 1
print(count)

