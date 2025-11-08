# 10**8 operation take 1 second
# hashing is used to reduce time complexity
'''hashing is a technique used to efficiently store and retrieve data by 
mapping input keys to fixed-size output values (hash codes) using a mathematical function,'''
n=[1,10,3,4,5,5,7,8,5,10]
nums = [1, 2,  3,  4, 5,10]
frequency_map = dict()

for i in range(len(n)):
    if n[i] in frequency_map:
        
        
        
        
        frequency_map[n[i]] += 1
    else:
        frequency_map[n[i]] = 1
for i in nums:
    if i in frequency_map:
        print(f"{i}:{frequency_map[i]}")
    else:
        print(f"{i}:0")
        
