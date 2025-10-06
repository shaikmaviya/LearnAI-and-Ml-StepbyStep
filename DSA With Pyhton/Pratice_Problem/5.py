s = "Mr Ding"

for i in s.split():
    reversed_text = i[::-1]
    text = " ".join(reversed_text)
print(text) 