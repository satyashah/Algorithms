

def two_pointers(arr, x):
    i = 0
    j = len(arr) - 1

    while i < j:
        
        sum = arr[i] + arr[j]

        if sum == x:
            return i,j
        elif sum > x:
            j -= 1
        else:
            i += 1

    return -1, -1

arr = [2, 3, 5, 8, 9, 10, 11]
val = 17

arrSize = len(arr)
arr.sort()

print(two_pointers(arr, val))
