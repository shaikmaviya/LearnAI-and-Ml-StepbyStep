n=153
num = n
return_value = 0
while n > 0:
    digit = n % 10
    n = n // 10
    quibe = digit ** 3
    return_value = return_value + quibe
if return_value == num:
    print("armstrong number")
else:
    print("not armstrong number")