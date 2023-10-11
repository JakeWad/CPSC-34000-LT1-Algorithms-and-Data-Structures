myname = "Your name"

def merge_and_count(arr, left, mid, right):
    inv_count = 0
    
    # Create temporary arrays for the left and right halves
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]
    
    # Initialize pointers and indices
    i = j = 0
    k = left
    
    # Merge the two halves
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
            # If an element in the left half is greater than in the right half,
            # it's an inversion, so increment the inversion count.
            inv_count += len(left_arr) - i
        k += 1
    
    # Copy any remaining elements from the left and right halves
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    
    return inv_count

def merge_sort_and_count(arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        # Recursively call merge_sort_and_count for left and right halves
        inv_count += merge_sort_and_count(arr, left, mid)
        inv_count += merge_sort_and_count(arr, mid+1, right)
        # Merge the two halves and count inversions
        inv_count += merge_and_count(arr, left, mid, right)
    
    return inv_count

def count_inversions(input_list):
    arr = input_list.copy()
    return merge_sort_and_count(arr, 0, len(arr) - 1)

# Example usage:
if __name__ == "__main__":    
    input_list = [5,4,3,2,1]
    print(count_inversions(input_list))  # Output: 10
 
    input_list = [1,5,2, 8,3,4]
    print(count_inversions(input_list))  # Output: 5
 
    input_list = [1,2,3,4,5]
    print(count_inversions(input_list))  # Output: 0
    
    input_list = [1,2,3,5,4]
    print(count_inversions(input_list))  # Output: 1
