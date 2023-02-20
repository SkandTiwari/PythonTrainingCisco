
# The following program finds out the largest number in the matrix


matrix =    [[23, 12, 21],
             [63, 70, 11],
             [45, 90, 22]]

result = []

for item in matrix:
    item.sort()
    temp = item[2]
    result.append(temp)

result.sort()
print(result[2])



#bonus question :- program to remove duplicates from a list


values = [1, 2, 2, 3, 4, 4 ,4, 5, 6, 7]


for i in range(1, 10):
    if values[i-1] == values[i]:
        values.pop(i-1)

print(values)
