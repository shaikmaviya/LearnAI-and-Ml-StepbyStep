num = [5,7,3,2,6,1,5,9]

# def reverse(num,left,right):
#     if left>=right:
#         return
#     num[left],num[right]=num[right],num[left]
#     reverse(num,left+1,right-1)
#     return num

# left=0
# right=len(num)-1

# while left<right:
#     num[left],num[right]=num[right],num[left]
#     left+=1
#     right-=1
# print(num)

for i in range(len(num)//2):
    num[i],num[len(num)-1-i]=num[len(num)-1-i],num[i]
print(num)
