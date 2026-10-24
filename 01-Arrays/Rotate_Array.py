# LeetCode 189 — Rotate Array

## Problem Statement

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

The array must be modified in-place.

### Example

```python
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

# Output
[5, 6, 7, 1, 2, 3, 4]
```

### Key Observation

Rotating an array to the right by `k` positions means that each element moves to index:

```python
new_index = (old_index + k) % n
```

where `n = len(nums)`.

Since rotating an array by its length returns the same array, we use:

```python
k %= n
```

This also handles cases where `k > n`.

---

## Method 1: Python Slicing

### Code

```python
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return

        k %= n
        nums[:] = nums[-k:] + nums[:-k]
```

### Intuition

Split the array into two parts:

- `nums[-k:]` — the last `k` elements.
- `nums[:-k]` — all elements before the last `k`.

Concatenate these parts in reverse order.

For example:

```python
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

nums[-3:]  # [5, 6, 7]
nums[:-3]  # [1, 2, 3, 4]

# Result
[5, 6, 7, 1, 2, 3, 4]
```

### Why use `nums[:]`?

`nums[:] = ...` replaces the contents of the existing list rather than assigning a new list to the local variable `nums`.

This is useful when the problem requires modifying the original list in-place.

### Complexity

- Time: `O(n)`
- Extra space: `O(n)`, because slicing and concatenation create temporary lists.

**Use:** A concise, Pythonic solution when extra memory is allowed.

---

## Method 2: Three Reversals (In-Place)

### Code

```python
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return

        k = k % n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
```

### Intuition

Instead of creating another array, reverse different portions of the original array.

Suppose:

```python
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
```

**Step 1: Reverse the entire array.**

```python
[7, 6, 5, 4, 3, 2, 1]
```

**Step 2: Reverse the first `k` elements.**

```python
[5, 6, 7, 4, 3, 2, 1]
```

**Step 3: Reverse the remaining elements.**

```python
[5, 6, 7, 1, 2, 3, 4]
```

The final array is rotated to the right by three positions.

### Why does it work?

Reversing the entire array puts the last `k` elements at the beginning, but reverses their internal order. Reversing the first `k` elements restores their order. Reversing the remaining elements restores the order of the other elements.

### Complexity

- Time: `O(n)`
- Extra space: `O(1)`

**Use:** Best when the problem requires in-place rotation with constant extra space.

---

## Method 3: Extra Array and Index Mapping

### Code

```python
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return

        k %= n
        result = [0] * n

        for i in range(n):
            result[(i + k) % n] = nums[i]

        nums[:] = result
```

### Intuition

Every element moves from its original index `i` to its destination index:

```python
(i + k) % n
```

Example:

```python
nums = [1, 2, 3, 4, 5]
k = 2
```

| Original index | Element | New index |
|---:|---:|---:|
| 0 | 1 | 2 |
| 1 | 2 | 3 |
| 2 | 3 | 4 |
| 3 | 4 | 0 |
| 4 | 5 | 1 |

Result:

```python
[4, 5, 1, 2, 3]
```

### Complexity

- Time: `O(n)`
- Extra space: `O(n)`

**Use:** Helps develop an understanding of index mapping and modular arithmetic.

---

## Method 4: Cyclic Replacements

### Code

```python
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return

        k %= n
        count = 0
        start = 0

        while count < n:
            current = start
            previous = nums[start]

            while True:
                next_index = (current + k) % n
                nums[next_index], previous = previous, nums[next_index]

                current = next_index
                count += 1

                if current == start:
                    break

            start += 1
```

### Intuition

Move an element directly to its destination, carrying the displaced element forward.

For example, with `nums = [1, 2, 3, 4, 5, 6]` and `k = 2`, the first element moves from index `0` to index `2`. The element displaced from index `2` then moves to index `4`, and the process continues until the cycle returns to its starting index.

Some elements form cycles with other elements. The algorithm starts a new cycle whenever necessary and tracks how many elements have been moved.

### Complexity

- Time: `O(n)`
- Extra space: `O(1)`

**Use:** Useful for learning cycle-based array manipulation and in-place algorithms.

---

## Method 5: Rotate One Step at a Time

### Code

```python
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return

        k %= n

        for _ in range(k):
            last = nums[-1]

            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]

            nums[0] = last
```

### Intuition

Each iteration rotates the array right by one position:

```python
[1, 2, 3, 4, 5]
# One rotation
[5, 1, 2, 3, 4]
# Two rotations
[4, 5, 1, 2, 3]
```

Repeat this process `k` times.

### Complexity

- Time: `O(n × k)`
- Extra space: `O(1)`

**Use:** Good for understanding the basic operation of rotation, but inefficient for large arrays.

---

## Comparison of All Methods

| Method | Time Complexity | Extra Space | In-place |
|---|---|---|---|
| Python slicing | `O(n)` | `O(n)` | No, in the strict auxiliary-space sense |
| Three reversals | `O(n)` | `O(1)` | Yes |
| Extra array | `O(n)` | `O(n)` | No, uses a separate array |
| Cyclic replacements | `O(n)` | `O(1)` | Yes |
| One step at a time | `O(n × k)` | `O(1)` | Yes |

## Important Edge Cases

### 1. `k = 0`

The array should remain unchanged.

### 2. `k = n`

The array should remain unchanged because `k % n == 0`.

### 3. `k > n`

Reduce `k` using `k %= n`.

### 4. Empty array

Check whether `nums` is empty before calculating `k % n` to avoid division by zero.

### 5. Single-element array

The array remains unchanged for any non-negative `k`.

---

## Final Notes

- Best for Python simplicity: Slicing.
- Best for in-place optimization:Three reversals.
- Best for understanding indices:Extra array.
- Best for exploring advanced in-place techniques:Cyclic replacements.
- Best for learning the basic operation:One-step rotation.

### Key Takeaway

The three-reversal algorithm is particularly important because it achieves `O(n)` time and `O(1)` extra space. Focus on understanding why the reversals work rather than memorizing the code.

Related concepts:Array manipulation, two pointers, modular arithmetic, in-place algorithms, time and space complexity.
