
def f(arr):
    for i in range(10//2):
        tmp = arr[i]
        arr[i] = arr[10-1-i]
        arr[10 - 1 - i] = tmp
    return arr

arr = [i for i in range(10)]

print(f(arr))