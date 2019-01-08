def bubble_sort(a):
    n= len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

A=[1,5,9,2,0,3]
bubble_sort(A)
A