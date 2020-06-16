def quicksort(data):
  # BASE CASE
  if len(data) <= 1:
    return data

  # Partition the data  
  # First item will be the pivot
  # Create storage for LHS and RHS
  pivot = data[0]
  left_side = []
  right_side = []

  # Loop through each item
  for current in data[1:]:   
    # Move all elements smaller, or equal, than the pivot to the LHS
    if current <= pivot:
      left_side.append(current)
    # Move all elements larger than the pivor to the RHS
    if current > pivot:
      right_side.append(current)
  
  # Recursively sort LHS and RHS until base case (a side contains a single element)
  return quicksort(left_side) + [pivot] + quicksort(right_side)

# def partition(data):
#   # Partition the data
#   # Start by choosing a pivot (choose the first item in the list)
#   pivot = data[0]
#   # We need to create storage for the LHS and the RHS
#   left = []
#   right = []
# ​
#   # We need to loop through each item
#   for current in data[1:]:
#       # if it's smaller or equal, append to left
#       if current <= pivot:
#           left.append(current)
#       # if it's bigger, add to RHS storage
#       else:
#           right.append(current)
# ​
#   return left, right, pivot
# ​
# ​
# # What kind of input will we get?
# # We expect a list
# def quicksort(data):
#     # check if data has 1 or 0 elements
#     # (base case) a side only contains a single element
#     if len(data) <= 1:
#         return data
# ​
#     left, right, pivot = partition(data)
# ​
#     # (recursive case) Recursively Quick Sort LHS and RHS until
#     return quicksort(left) + [pivot] + quicksort(right)
# ​
# ​
# print(quicksort([2,5,7,1,3,4,6,9,8]))