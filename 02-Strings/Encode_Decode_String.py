# LeetCode 271 — Encode and Decode Strings

## Problem Statement

Design an algorithm to encode a list of strings into a single string and decode it back to the original list.

The encoding must preserve the original strings, even if they contain special characters such as `#`.

### Example

```python
Input:  ["Hello", "World"]
Encoded: "5#Hello5#World"
Output: ["Hello", "World"]
```

## Approach: Length-Prefixed Encoding

### Code

```python
strs = ["Hello", "World"]

# Encode strings
result = ""

for word in strs:
    result += str(len(word)) + "#" + word

print(result)

# Decode the encoded string
i = 0
l = []

while i < len(result):
    j = result.find("#", i)

    length = int(result[i:j])
    word = result[j + 1:j + 1 + length]

    l.append(word)

    i = j + 1 + length

print(l)
```

### Intuition

Instead of separating words using spaces or another delimiter, store the length of each word followed by `#` and the word itself.

For example:

```text
["Hello", "World"] → "5#Hello5#World"
```

During decoding:

- `i` marks the beginning of the length prefix.
- `j` finds the position of `#`.
- `result[i:j]` extracts the length.
- `result[j + 1:j + 1 + length]` extracts the actual word.
- `i` moves to the beginning of the next encoded word.

This approach also handles strings containing `#` because the decoder uses the stored length rather than treating every `#` as a separator.

### Dry Run

Encoded string:

```text
5#Hello5#World
```

| Step | `i` | `j` | Length | Extracted word |
|---|---:|---:|---:|---|
| 1 | 0 | 1 | 5 | `Hello` |
| 2 | 7 | 8 | 5 | `World` |

Final output:

```python
["Hello", "World"]
```

## Complexity Analysis

Let `n` be the total number of characters in the encoded string.

- **Time complexity:** `O(n)` — encoding and decoding process each character a constant number of times, assuming efficient string construction.
- **Auxiliary space complexity:** `O(n)` — the encoded string and decoded list require space proportional to the input size.

*Note:* Repeated string concatenation with `+=` can take more than linear time in some situations. Using a list and `"".join()` makes encoding more reliably efficient.

## Important Observations

1. **Why store the length?** It tells the decoder exactly how many characters belong to each word.
2. **Why use `result[i:j]`?** It supports multi-digit lengths, unlike `int(result[j - 1])`, which reads only one digit.
3. **Why update `i` this way?** `i = j + 1 + length` skips the delimiter and the complete word.
4. **Why not split using `#`?** A string may already contain `#`, so splitting could incorrectly separate its contents.

## Summary

Length-prefixed encoding converts a list of strings into one string by storing each word's length before its content. Decoding uses that length to reconstruct the original list without ambiguity.

**Use:** This technique is useful in serialization, network protocols, and storing variable-length strings when the data may contain delimiter characters.
