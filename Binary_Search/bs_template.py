# RECURSIVELY
def binary_search_recursive(arr, low, high, x):		
    if high >= low:
        mid = (high + low) // 2 # Get the middle value (floored)
        
        if arr[mid] == x: # If element is present at the middle itself
            return mid
        elif arr[mid] > x: # If element is smaller than mid, then check left subarray
            return binary_search_recursive(arr, low, mid - 1, x)
        else: # Else the element can only be present in right subarray
            return binary_search_recursive(arr, mid + 1, high, x) 
    else:
        return -1 # Incase value is not in list
    
#ITERATIVE
def binary_search_iterative(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        
        if arr[mid] < x: # If x is greater, ignore left half 
            low = mid + 1
        elif arr[mid] > x: # If x is smaller, ignore right half
            high = mid - 1
        else: # means x is present at mid
            return mid
    
    return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result_recur = binary_search_recursive(arr, 0, len(arr)-1, x)
print(result_recur)

result_iter = binary_search_iterative(arr, x)
print(result_iter)