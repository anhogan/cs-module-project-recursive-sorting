def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Start with arrA[0] and arrB[0], compare the values and add the smallest to merged_arr at 0 index
    # Increment the index on the arr from which the element was taken by one and repeat

    print(merged_arr)
    return merged_arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr4 = [0, 1, 2, 3, 4, 5]
merge(arr1, arr4)

def merge_sort(arr):
    # BASE CASE: len(arr) == 1
    # While not base, split arr in two sides (L / R) until each element is it's own arr
    # Once each arr is one element, merge them together    

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass