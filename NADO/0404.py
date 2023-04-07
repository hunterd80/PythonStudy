txt = input("암호화할 텍스트 : ")
key = int(input("암호화 키 : "))

result = ""
for c in txt:
    if c >= 'A' and c <= 'Z':
        c2 = ord(c) + key
        if c2 > ord('Z'):
            c2 = c2 - 26
    else:
        c2 = ord(c)


    result = result + chr(c2)
print(result)

result2 = ""
for c in result:
    if c >= 'A' and c <= 'Z':
        c2 = ord(c) - key
        if c2 < ord('A'):
            c2 = c2 - 26
    else:
        c2 = ord(c)


    result2 = result2 + chr(c2)
print(result2)