s="momom"
left=0
right=len(s)-1

while left<right:
    if s[left]!=s[right]:
        print("not a palindrome")
        break
    left+=1
    right-=1
    
else:
    print("palindrome")     

    
def is_palindrome(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return is_palindrome(s,left+1,right-1)

print(is_palindrome(s,left,right))


    