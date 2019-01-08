def insertion_sort(A):
    n= len(A)
    for i in range(n):
        key = A[i]
        j= i - 1
        while j>=0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
A= [1,2,7,6,2,0,1]
insertion_sort(A)
A