
"""
# LeetCode 49 — Group Anagrams

## Problem Statement

Given an array of strings, group the anagrams together.
You can return the answer in any order.

### Example

Input:
["eat", "tea", "tan", "ate", "nat", "bat"]

Output:
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

## Approach: Character Frequency + HashMap

### Intuition

Anagrams contain exactly the same characters with the
same frequencies.

For each word:
1. Create an array of 26 zeros to count letters a-z.
2. Count each character using ord(char) - ord('a').
3. Convert the frequency array into a tuple.
4. Use the tuple as a HashMap key and append the word
   to its corresponding group.
5. Return all groups.

### Code

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            res[tuple(count)].append(word)

        return list(res.values())

### Dry Run

Input:
["eat", "tea", "tan", "ate", "nat", "bat"]

| Word | Character counts | Group |
|------|------------------|-------|
| eat  | e:1, a:1, t:1    | Group 1 |
| tea  | e:1, a:1, t:1    | Group 1 |
| tan  | t:1, a:1, n:1    | Group 2 |
| ate  | a:1, t:1, e:1    | Group 1 |
| nat  | n:1, a:1, t:1    | Group 2 |
| bat  | b:1, a:1, t:1    | Group 3 |

Final groups:
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

## Complexity Analysis

- Time Complexity: O(n * k)
  Each character is counted once, and each word's
  frequency tuple has a fixed length of 26.

- Auxiliary Space Complexity: O(n)
  The HashMap stores at most n distinct frequency keys.
  Each key has a fixed size of 26.

Here:
n = number of words
k = maximum length of a word

The returned groups require additional O(n * k) space.

## Important Observations

1. defaultdict(list) automatically creates an empty list
   for a new key.
2. Lists cannot be dictionary keys because they are mutable.
   Converting count into a tuple makes it hashable.
3. Anagrams have identical character-frequency tuples.
4. Sorting each word is another approach, but frequency
   counting avoids sorting individual words.
5. This implementation assumes lowercase English letters
   from a to z.

## Summary

Group Anagrams uses a HashMap with character-frequency
tuples to group words efficiently.

Time: O(n * k)
Auxiliary Space: O(n)

Pattern:
Character Frequency -> Tuple -> HashMap Grouping

Use:
This pattern is useful when grouping strings by character
composition, such as anagrams and frequency-based problems.
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            res[tuple(count)].append(word)

        return list(res.values())


if __name__ == "__main__":
    solution = Solution()

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strs))
