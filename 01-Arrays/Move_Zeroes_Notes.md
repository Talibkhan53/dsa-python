# Move Zeroes
Platform:LeetCode  
Topic:Arrays  
Pattern:Two Pointers / In-place Array Modification  
Difficulty:Easy

## 1. Problem Understanding

Given an integer array, move all zeroes to the end while maintaining the relative order of the non-zero elements.

The operation must modify the original array in place.

Example:

- Input: `[0, 1, 0, 3, 12]`
- Output: `[1, 3, 12, 0, 0]`

## 2. Approach 1: Two Pointers with Swapping

### Logic

1. Initialize `k = 0` to represent the next position for a non-zero element.
2. Iterate through the array using `i`.
3. Whenever `nums[i]` is non-zero, swap it with `nums[k]`.
4. Increment `k`.
5. Continue until every element has been checked.

### Why it works

Every non-zero element is moved to the next available position at the beginning of the array. Their relative order is maintained, and zeroes are pushed toward the end.

### Complexity

- Time: O(n)
- Auxiliary space: O(1)

## 3. Approach 2: Overwrite Non-Zero Elements

### Logic

1. Use `k` to track the next position for a non-zero element.
2. Copy each non-zero element into `nums[k]`.
3. Increment `k` after each copy.
4. After processing all elements, fill the remaining positions with zeroes.

### Why it works

The first pass collects all non-zero elements in their original order. The second pass fills the unused positions with zeroes.

### Complexity

- Time: O(n)
- Auxiliary space: O(1)

## 4. Approach 3: Sorting

### Logic

1. Sort the array using `nums.sort(key=lambda x: x == 0)`.
2. The sorting key evaluates to `False` for non-zero elements and `True` for zeroes.
3. Python places `False` before `True`, moving zeroes to the end.

### Why it works

The sorting key separates non-zero values from zeroes. Python's stable sort preserves the relative order of elements with equal keys.

### Complexity

- Time: O(n log n) as the general sorting bound.
- Auxiliary space: Python's sorting implementation uses additional temporary memory.

Limitation: Sorting is less efficient than the linear-time two-pointer approaches and is not the intended technique for this problem.

## 5. Comparison of Approaches

| Approach | Time | Auxiliary Space | Main Idea |
|---|---|---|---|
| Swapping | O(n) | O(1) | Swap non-zero values forward |
| Overwriting | O(n) | O(1) | Copy non-zero values, then fill zeroes |
| Sorting | O(n log n) general bound | Implementation-dependent | Sort by whether a value is zero |

## 6. What I Learned

- Two pointers can modify an array in place.
- A position pointer can track where the next valid element belongs.
- Overwriting can avoid unnecessary swaps.
- Sorting can solve the problem, but it is not always the most efficient algorithm.
- The relative order of non-zero elements must be preserved.
