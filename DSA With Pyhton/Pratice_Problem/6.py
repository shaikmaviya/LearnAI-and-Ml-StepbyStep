
s="abcdefg"
def reverseStr(s,k):
    lenth=len(s)
    s=list(s)
    for i in range(0,lenth,2*k):
        left=i
        right=min(i+k,lenth)-1
        while left<right:
            s[left],s[right-1]=s[right-1],s[left]
            left+=1
            right-=1
    return "".join(s)
        

reversed=reverseStr(s,3)
print(reversed)