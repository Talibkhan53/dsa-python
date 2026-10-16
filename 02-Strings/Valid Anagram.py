
class Solution:

    # Approach 1: Using Two Dictionaries
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            t_count[t[i]] = t_count.get(t[i], 0) + 1

        return s_count == t_count

    # Approach 2: Using Sorting
    def isAnagramSort(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t

    # Approach 3: Using One Dictionary
    def isAnagramOneDict(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}

        # Count characters in the first string
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Subtract characters using the second string
        for char in t:
            if char not in char_count:
                return False

            char_count[char] -= 1

        return all(count == 0 for count in char_count.values())


# Testing the approaches
solution = Solution()

print(solution.isAnagram("tac", "cat"))
print(solution.isAnagramSort("tac", "cat"))
print(solution.isAnagramOneDict("tac", "cat"))
