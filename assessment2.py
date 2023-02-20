matrix = [[1, 2, 3], [4, 5, 6], [7, 8 , 9]]

dir = 0
t = 0
b = len(matrix)-1
l = 0
r = len(matrix[0])-1

ans = []

while(l <= r and t <= b):
    if dir == 0:
        for i in range(l, r+1):
            ans.append(matrix[t][i])
        t+=1

    elif dir == 1:
        for i in range(t, b+1):
            ans.append(matrix[i][r])
        r-=1
    elif dir == 2:
        for i in range(r, l-1, -1):
            ans.append(matrix[b][i])
        b-=1
    elif dir == 3:
        for i in range(b, t-1, -1):
            ans.append(matrix[i][l])
        l+=1
    dir = (dir+1)%4

print(ans)



