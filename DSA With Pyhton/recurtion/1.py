def funtion(sum,i,n):
    if i>n:
        return sum
    return funtion(sum+i,i+1,n)

print(funtion(0,1,4))



def fun(n):
    if n==1:
        return 1
    return n+fun(n-1)
x=fun(4)
print(x)