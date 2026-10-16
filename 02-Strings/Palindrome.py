
class Solution:
    # Approach 1: Manual filtering
    def isPalindromeManual(self, s: str) -> bool:
        new_str = ''
        symbols = [
            '?', ',', '.', '!', ':', ' ', '/', '@', '#',
            '-', '(', ')', '[', ']', '{', '}', '\\',
            "'", '"', ';', '_', '+', '=', '*', '&',
            '^', '%', '$', '~', '`', '<', '>', '|'
        ]

        for char in s.lower():
            if char not in symbols:
                new_str += char

        i = 0
        j = len(new_str) - 1

        while i < j:
            if new_str[i] != new_str[j]:
                return False
            i += 1
            j -= 1

        return True

    # Approach 2: Using Python's built-in function
    def isPalindromeBuiltIn(self, s: str) -> bool:
        new_str = ''

        for char in s.lower():
            if char.isalnum():
                new_str += char

        i = 0
        j = len(new_str) - 1

        while i < j:
            if new_str[i] != new_str[j]:
                return False
            i += 1
            j -= 1

        return True
