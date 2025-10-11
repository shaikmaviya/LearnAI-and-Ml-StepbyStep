head = [1,1,2,3,3]
result = []
for x in head:
    if not result or result[-1] != x:
        result.append(x)
