# LeetCode 36 — Valid Sudoku

## Problem Statement

Determine if a 9 × 9 Sudoku board is valid.

A Sudoku board is valid if:

1. Each row contains no duplicate digits from 1–9.
2. Each column contains no duplicate digits from 1–9.
3. Each of the nine 3 × 3 sub-boxes contains no duplicate digits from 1–9.

Empty cells are represented by `"."`.

**Note:** A valid Sudoku board does not necessarily mean it is solvable.

## Approach: Hash Set + Hash Map

### Code

```python
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):

                val = board[r][c]

                if val == ".":
                    continue

                # Identify the current 3x3 box
                box_key = (r // 3, c // 3)

                # Check for duplicates
                if (val in rows[r] or
                    val in cols[c] or
                    val in squares[box_key]):
                    return False

                # Store the value
                rows[r].add(val)
                cols[c].add(val)
                squares[box_key].add(val)

        return True
```

### Intuition

The main idea is to use three separate collections of sets to track the numbers already encountered in each row, column, and 3 × 3 box.

We use sets because they allow average `O(1)` lookup time and automatically prevent duplicate storage.

**1. Row Tracking**

```python
rows = collections.defaultdict(set)
```

Each row maintains its own set of numbers.

For example:

```python
rows[0] = {"5", "3", "7"}
```

Before inserting a number, we check whether it already exists in that row.

**2. Column Tracking**

```python
cols = collections.defaultdict(set)
```

Each column maintains its own set of numbers.

For example:

```python
cols[0] = {"5", "6", "8"}
```

This helps us identify duplicate numbers in the same column.

**3. 3 × 3 Box Tracking**

```python
squares = collections.defaultdict(set)
```

We identify each 3 × 3 box using:

```python
box_key = (r // 3, c // 3)
```

Integer division groups row and column indices into their respective boxes.

For example:

| Row | Column | Box Key |
|---:|---:|---|
| 0 | 0 | (0, 0) |
| 1 | 2 | (0, 0) |
| 2 | 1 | (0, 0) |
| 3 | 3 | (1, 1) |
| 6 | 6 | (2, 2) |

This gives us nine unique box identifiers.

**4. Duplicate Checking**

```python
if val in rows[r] or val in cols[c] or val in squares[box_key]:
    return False
```

Before inserting a number, we check all three conditions.

If the number already exists in any one of them, the Sudoku board is invalid.

Otherwise, we insert it into all three sets.

## Dry Run

Consider inserting `"5"` at position `(0, 0)`.

Initially:

```python
rows[0] = set()
cols[0] = set()
squares[(0, 0)] = set()
```

| Operation | Result |
|---|---|
| Check `5` in row 0 | Not found |
| Check `5` in column 0 | Not found |
| Check `5` in box (0, 0) | Not found |
| Insert `5` into all three sets | Successful |

Now suppose another `"5"` appears at position `(0, 4)`.

- Row 0 already contains `"5"`.
- Duplicate detected.
- Return `False`.

## Complexity Analysis

Let the Sudoku board have dimensions 9 × 9.

- **Time Complexity:** `O(1)` — exactly 81 cells are checked, and set lookups and insertions take average `O(1)` time.
- **Auxiliary Space Complexity:** `O(1)` — the board has a fixed size, and we store at most 81 values across the tracking sets.

For a generalized Sudoku board of size `n × n`, the complexity would be `O(n²)` time and `O(n²)` auxiliary space.

## Important Observations

1. **Why use defaultdict(set)?** It automatically creates an empty set whenever a new row, column, or box key is accessed.
2. **Why use three separate collections?** Each collection tracks a different Sudoku constraint.
3. **Why use `(r // 3, c // 3)`?** It uniquely identifies which 3 × 3 box contains the current cell.
4. **Why skip `"."`?** Empty cells do not participate in duplicate checking.
5. **Why check before inserting?** This ensures we detect duplicates before modifying our tracking structures.

## Summary

The Hash Set approach validates Sudoku by maintaining separate sets for rows, columns, and 3 × 3 boxes. Every filled cell is checked against all three constraints before being inserted.

**Use:** This technique is useful in constraint validation problems, duplicate detection, grid-based problems, and situations where multiple independent conditions must be tracked efficiently.
