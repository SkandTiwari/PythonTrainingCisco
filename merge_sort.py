"""Merge sort is the most optimised algorithm for sorting based on divide and conquer strategy. 
It can be implemented using recursion. the recursive call will take place untill only a single element is left"""

A = [6, 4, 5, 3]
l = 0
r = len(A)-1

def merge_sort(A, l, r):
    if l < r:
        m = (l+r)//2          # Dividing the list
        merge_sort(A, l, m)   # Breaking-down the first half
        merge_sort(A, m+1, r) # Breaking-down the second half
        merge_list(A,l,m,r)


def merge_list(A, l, m, r):
    leftList = A[l:m]
    rightList = A[m:r]
    k = l
    i = 0
    j = 0

    while(l+i < m and m+j < r):
        if(leftList[i] <= rightList[j]):
            A[k] = leftList[i]
            i+=1

        else:
            A[k] = rightList[j]
            j+=1
        k+=1
    if l+i < m:
        A[k] = leftList[i]
        i+=1
        k+=1
    else:
        while k< r:
            A[k] = rightList[j]
            j += 1
            k += 1

