# LeetCode 15 — 3Sum

## Problem Statement

Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that:

1. `i`, `j`, and `k` are distinct indices.
2. `nums[i] + nums[j] + nums[k] == 0`.
3. The solution must not contain duplicate triplets.

**Example:**

```python
nums = [-1, 0, 1, 2, -1, -4]
```

**Output:**

```python
[[-1, -1, 2], [-1, 0, 1]]
```

---

## Approach 1: Brute Force (Three Nested Loops)

### Code

```python
class Solution:
    def threeSum(self, nums):

        result = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):

                    if nums[i] + nums[j] + nums[k] == 0:

                        triplet = sorted([nums[i], nums[j], nums[k]])

                        if triplet not in result:
                            result.append(triplet)

        return result
```

### Intuition

The brute-force approach checks every possible combination of three numbers.

We use three nested loops:

- `i` selects the first number.
- `j` selects the second number.
- `k` selects the third number.

If their sum equals zero, we have found a valid triplet.

We use `sorted()` to maintain a consistent order and avoid duplicate combinations.

### Important Observations

1. `j = i + 1` ensures that we don't reuse the same index.
2. `k = j + 1` ensures that all three indices are distinct.
3. `sorted()` helps identify duplicate triplets.
4. `triplet not in result` prevents storing the same triplet again.

### Complexity Analysis

- **Time Complexity:** O(n³) for checking combinations, excluding duplicate-list lookup and sorting overhead.
- **Auxiliary Space Complexity:** O(1) excluding the output and temporary triplet.

**Use:** Useful for understanding the problem and learning how to generate combinations using nested loops.

---

## Approach 2: Sorting + Two Pointers

### Code

```python
class Solution:
    def threeSum(self, nums):

        nums.sort()
        result = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:

                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result
```

### Intuition

Instead of checking every possible combination, we sort the array and use two pointers to find the remaining two numbers.

First, we sort the array:

```python
[-4, -1, -1, 0, 1, 2]
```

We use three variables:

- `i` fixes the first number.
- `left` points to the next available number.
- `right` points to the last number.

We calculate:

```python
total = nums[i] + nums[left] + nums[right]
```

Based on the result:

1. If `total == 0`, we found a valid triplet.
2. If `total < 0`, move `left` forward to increase the sum.
3. If `total > 0`, move `right` backward to decrease the sum.

### Dry Run

Consider:

```python
nums = [-1, 0, 1, 2, -1, -4]
target = 0
```

After sorting:

```python
[-4, -1, -1, 0, 1, 2]
```

**Iteration 1:**

`i = 0`, `left = 1`, `right = 5`

```python
-4 + (-1) + 2 = -3
```

Sum is smaller than zero, so move `left` forward.

Continue moving `left` until it reaches the end. No triplet is found for `i = 0`.

**Iteration 2:**

`i = 1`, `left = 2`, `right = 5`

```python
-1 + (-1) + 2 = 0
```

First triplet found:

```python
[-1, -1, 2]
```

Move both pointers:

```python
left += 1
right -= 1
```

Now:

```python
-1 + 0 + 1 = 0
```

Second triplet found:

```python
[-1, 0, 1]
```

Move both pointers again. The pointers cross, so the loop ends.

**Duplicate handling:**

```python
if i > 0 and nums[i] == nums[i - 1]:
    continue
```

Skips duplicate first numbers.

The two inner `while` loops skip duplicate left and right values after finding a triplet.

### Complexity Analysis

- **Time Complexity:** O(n²) — sorting takes O(n log n), and the nested pointer traversal takes O(n²).
- **Auxiliary Space Complexity:** O(1) excluding the output, assuming an in-place sort.

**Use:** This is the standard optimized solution for Three Sum and an important application of the Two Pointers technique.

---

## Approach 3: Hash Set

### Code

```python
class Solution:
    def threeSum(self, nums):

        result = []

        for i in range(len(nums)):

            seen = set()

            for j in range(i + 1, len(nums)):

                third = -nums[i] - nums[j]

                if third in seen:

                    triplet = sorted([nums[i], nums[j], third])

                    if triplet not in result:
                        result.append(triplet)

                seen.add(nums[j])

        return result
```

### Intuition

Instead of using three nested loops, we fix one number and use a Hash Set to find the remaining two numbers.

We calculate the required third number:

```python
third = -nums[i] - nums[j]
```

Then we check whether that number already exists in our set.

If it exists, we have found a valid triplet.

### Dry Run

Consider:

```python
nums = [-1, 0, 1, 2, -1, -4]
```

Initially:

```python
i = 0
nums[i] = -1
seen = set()
```

Now the inner loop starts from `i + 1`.

| j | nums[j] | third | seen before check | Found? |
|---|---:|---:|---|---|
| 1 | 0 | 1 | {} | No |
| 2 | 1 | 0 | {0} | Yes |
| 3 | 2 | -1 | {0, 1} | No |
| 4 | -1 | 1 | {0, 1, 2} | Yes |

At `j = 2`:

```python
third = -(-1) - 1
third = 0
```

Since `0` already exists in the set, we found:

```python
[-1, 1, 0]
```

After sorting:

```python
[-1, 0, 1]
```

### Important Observations

1. `i` fixes the first number.
2. `j` selects the second number.
3. `third` calculates the required third number.
4. `seen` stores previously encountered numbers.
5. `j` starts from `i + 1` to ensure distinct indices.
6. We use `triplet not in result` to avoid duplicate results.

### Complexity Analysis

- **Time Complexity:** O(n²) average for set lookups, plus duplicate checking and sorting overhead.
- **Auxiliary Space Complexity:** O(n) for the Hash Set, excluding output.

**Use:** Helps understand how Hash Sets can replace an inner loop through efficient lookup.

---

## Comparison of All Three Approaches

| Approach | Time Complexity | Main Technique |
|---|---|---|
| Brute Force | O(n³) | Three nested loops |
| Two Pointers | O(n²) | Sorting + Two Pointers |
| Hash Set | O(n²) average | Hash Set lookup |

## Important Observations

1. **Why use sorting in Two Pointers?** Sorting allows us to increase or decrease the sum intelligently by moving pointers.
2. **Why use `i + 1`?** It prevents reusing the same array index.
3. **Why skip duplicates?** The problem requires unique triplets, not repeated combinations.
4. **Why use a set?** Sets provide average O(1) membership checking.
5. **Why use `third`?** It calculates the exact number required to make the sum zero.

## Summary

Three Sum teaches three important problem-solving techniques:

- Brute Force: Generate every possible combination.
- Two Pointers: Use sorting to reduce the number of operations.
- Hash Set: Use efficient lookups to eliminate an inner loop.

**My conclusion:** The Sorting + Two Pointers approach is the preferred solution to remember for LeetCode 15. The other two approaches are useful for understanding how optimization works and when Hash Sets can replace nested loops.
