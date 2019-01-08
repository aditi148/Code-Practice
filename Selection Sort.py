def sel_sort(a):
    n= len(a)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]

A= [1,2,7,6,2,0,1]
sel_sort(A)
A