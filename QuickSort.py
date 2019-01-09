a = [5,2,1,9,3,0]
def partition(a, low, high):
    i=low-1
    pivot = a[high]
    for j in range(low, high):
        if a[j] <= pivot:
            i=i+1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[high] = a[high], a[i+1]
    return(i+1)

def quick_sort(a, low, high):
    if low< high:
        pi= partition(a, low, high)
        quick_sort(a, low, pi-1)
        quick_sort(a, p+1, high)
