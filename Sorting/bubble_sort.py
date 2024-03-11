
arr = [8, 3, 2, 1, 0]
print("Start: {}".format(arr))

for i in range(len(arr) - 1): # -1 to convert len to index and Not inclusive of the end! (imagine -1)
    for j in range(len(arr) - 1 - i): # -1 to convert len to index, -i since last i values are sorted, Not inclusive of the end! (imagine -1) 
        if arr[j] > arr[j+1]: # Swap values
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
    print("Pass {}: {}".format(i, arr))

print(arr)