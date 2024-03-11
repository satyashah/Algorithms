
A = [8, 3, 5, 1, 0]
print("Start: {}".format(A))


for i in range(1,len(A)): # Unlike bubble sort the begining i elements are sorted so we start at 1 to the end
    key = A[i] # Must set to key since A[i] value will change
    j = i - 1 # Compare to the index before
    while j>=0 and A[j] > key: 
        A[j+1] = A[j] #Converts the index after j to j
        j = j - 1
        print("\tPass {}.{}: {}".format(i, j+1, A))
    A[j+1] = key # Since the while loop will stop at one before i (j = j-1) we need to use j + 1
    print("Pass {}: {}".format(i, A))

print(A)
