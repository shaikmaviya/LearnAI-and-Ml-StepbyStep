cubeofthree=[]
for num in range(0, 1000):
    cube = num ** 3
    cubeofthree.append(cube)


def isPowerOfThree(cubelist):
    if n==0 or n<=0:
        return False
    elif n in cubelist:
        return True
    else:
        while n%3 == 0:
            n = n // 3
        return True

result = isPowerOfThree(cubeofthree)
print(result)  # This will print: True