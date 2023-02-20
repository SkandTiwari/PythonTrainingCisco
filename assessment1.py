inp1 = input("Input1 : ")
inp2 = input("Input2 : ")
i = 0
req = -1
for ch in inp1:
    if (ch in inp2) and (inp2.index(ch) >= i) :
        i+=1
        continue
    else:
        temp = abs(ord(ch)-ord(inp2[i]))
    if req < temp :  
        req = temp
    i+=1

print(req)
 