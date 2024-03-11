from typing import List


def isPairSum(A: List[int], N: int, X: int) -> bool:
	
    # represents first pointer
	i = 0
	# represents second pointer
	j = N - 1

	while i < j:
		# If we find a pair
		if A[i] + A[j] == X:
			return i,j

		# If sum of elements at current
		# pointers is less, we move towards
		# higher values by doing i++
		elif A[i] + A[j] < X:
			i += 1

		# If sum of elements at current
		# pointers is more, we move towards
		# lower values by doing j--
		else:
			j -= 1

	return -1, -1

arr = [2, 3, 5, 8, 9, 10, 11]
val = 17

arrSize = len(arr)
arr.sort()

print(isPairSum(arr, arrSize, val))
