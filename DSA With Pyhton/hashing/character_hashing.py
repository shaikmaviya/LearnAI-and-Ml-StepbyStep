s="azfhlejsaszjfh"
q=['s','z','a','j','f','h','l','e']
for char in s:
    if char in q:
        print(f"{char}:{s.count(char)}")
    else:
        print(f"{char}:0")
for char in q:
    print(f"{char}:{s.count(char)}")