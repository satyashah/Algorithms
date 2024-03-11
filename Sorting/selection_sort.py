
A = [8, 3, 5, 1, 0]
print("Start: {}".format(A))

for i in range(0, len(A) - 1):
    min_indx = i
    for j in range(i+1, len(A)):
        if A[j] < A[min_indx]:
            min_indx = j
    
    temp = A[i]
    A[i] = A[min_indx]
    A[min_indx] = temp
    print("Pass {}: {}".format(i, A))

print(A)