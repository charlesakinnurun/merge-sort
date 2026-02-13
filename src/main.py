# %% [markdown]
# # Merge Sort

# %%
import time

# %%
def merge_sort(arr,depth=0):
    # Implementation of Merge Sort with visual tracking.
    # Args:
    #   arr: The list of elements to sort
    #   depth: Current recursion depth of visualization purposes

    # 1. ILLUSTRATION OF SPLITTING (DIVIDE)
    # We print the current state to show how the array is being broken down
    indent = " " * depth
    print(f"{indent}Splitting: {arr}")

    # BASE CASE: If the list has 1 or 0 elements, It is already sorted
    if len(arr) <= 1:
        return arr

    # 2. FINDING THE MIDDLE (DIVIDE)
    # We use floor division (//) to find the midpoint of the current array
    mid = len(arr) // 2

    # 3. RECURSIVE CALLS (CONQUER)
    # We split the array into two halves: left and right
    # We recursively call merge_sort on both halves until we hit the base case
    left_half = merge_sort(arr[:mid], depth= + 1)
    right_half = merge_sort(arr[mid:], depth + 1)

    # 4. MERGING THE HALVES (COMBINE)
    # After the recursive calls return, we merge the two sorted halves
    sorted_arr = merge(left_half,right_half)

    print(f"{indent}Merged: {sorted_arr}")
    return sorted_arr

# %%
def merge(left,right):
    # Helper function to merge two sorted list into one sorted list
    result = [] # This will store our merged, sorted elements
    i = 0 # Pointer for the left list
    j = 0 # Pointer for the right list

    # Compare elements from both lists and pick the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            # Elements in left is smaller, add it to result
            result.append(left[i])
            i += 1
        else:
            # Elements in right is smaller, add it to result
            result.append(right[j])
            j += 1

    # If there are remaining elements in left, add them to result
    # (One list might be longer or have larger elements left over)
    result.extend(left[i:])

    # If there are reamaining elements in right, add them to result
    result.extend(right[j:])

    return result

# %%
def run_demo():
    # Function to run various examples and show the algorithm in action

    print("="*60)
    print("MERGE SORT: DIVIDE AND CONQUER VISUALIZATION")
    print("="*60)
    print("\nConcept:")
    print("1. Divide: Split the unsorted list into n sublists")
    print("2. Conquer: Sort Sublists (base case is a list of size 1)")
    print("3. Combine: Merge sublists back together in sorted order")
    print("="*60)

    # Example 1: Standard Unsorted list
    example_1 = [38,27,43,3,9,82,10]
    print(f"Example 1: {example_1}")
    sorted_1 = merge_sort(example_1)
    print(f"\nFINAL SORTED LIST: {sorted_1}")
    print("="*60)

    # Example 2: List with duplicates
    example_2 = [5,1,9,5,8]
    print(f"Example 2 (Duplicates): {example_2}")
    sorted_2 = merge_sort(example_2)
    print(f"\nFINAL SORTED LIST: {sorted_2}")

    # Example 3: Already sorted list
    example_3 = [1,2,3,4,5]
    print(f"Example 3 (sorted): {example_3}")
    sorted_3 = merge_sort(example_3)
    print(f"\nFINAL SORTED LIST: {sorted_3}")
    print("="*60)

# %%
if __name__ == "__main__":
    # The entry point of the script
    run_demo()


