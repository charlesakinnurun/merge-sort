<h1>Merge Sort</h1>

## 🔎 Overview

<b>Merge Sort</b> is a popular divide and conquer algorithm.

It works by repeatedly splitting a list into smaller sublists, sorting them, and then merging them back together in order.

It is known for being:
-   ✅ Stable (keeps equal elements in original order)
-   ✅ Predictable O(n log n) performance
-   ✅ Efficient for large datasets
-   ❌ Uses extra memory (not in-place)





## ⚙️ How Merge Sort Works
### Step 1 — Divide

Split the array into two halves until each subarray has only one element.

Example:

[38, 27, 43, 3, 9, 82, 10]

Becomes:

[38, 27, 43]    [3, 9, 82, 10]

Then continues splitting until single elements remain.

### Step 2 — Conquer

Single-element arrays are already sorted.

### Step 3 — Merge

Merge the smaller arrays back together while sorting them.

Example merge:

[27] + [38]  →  [27, 38]
[3] + [9]    →  [3, 9]

Continue merging until the full sorted list is produced.

Final result:

[3, 9, 10, 27, 38, 43, 82]



### ⏱️ Time & Space Complexity
| ⏱️ Case       | Time Complexity |
|---------------|----------------|
| Best Case     | O(n log n)     |
| Average Case  | O(n log n)     |
| Worst Case    | O(n log n)     |


## 📁 Python Implementation
```python
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



```


### 👍 Advantages

-   Guarantees good performance even for large lists
-   Works well for linked lists
-   Easy to parallelize



### 👎 Disadvantages

-   Requires extra memory
-   Slower than quicksort for smal datasets
-   Recursive calls may increase overload


### 📌 When to Use Merge Sort

-   Sorting for large datasets
-   Stability matters
-   Working with linked lists
-   Parallel processing is needed


### 🏁 Summary
Merge Sort is a reliable, efficient sorting algorithm with consistent performance. While it uses extra memory, its stability and predictable runtime make it a stong choice for many applications
