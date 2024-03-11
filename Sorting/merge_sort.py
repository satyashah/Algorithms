
A = [8, 3, 5, 1, 0]
print("Start: {}".format(A))


def mergeSort(A):
    if len(A) > 1:
        m = len(A) // 2
        l = A[0:m]
        r = A[m:len(A)]
        
        l = mergeSort(l)
        r = mergeSort(r)
        # Merge lists together
        l_i, r_i, a_i = 0, 0, 0

        while l_i < len(l) and r_i < len(r):
            if l[l_i] < r[r_i]:
                A[a_i] = l[l_i]
                a_i += 1
                l_i += 1
            else:
                A[a_i] = r[r_i]
                a_i += 1
                r_i += 1

        while l_i < len(l):
            A[a_i] = l[l_i]
            a_i += 1
            l_i += 1
        while r_i < len(r):
            A[a_i] = r[r_i]
            a_i += 1
            r_i += 1
    return A

A_sorted = mergeSort(A)
print(A_sorted)

