
# Move Zeroes
# Problem: Move all zeroes to the end while maintaining
# the relative order of non-zero elements.

class Solution:

    # Approach 1: Two Pointers / Swapping
    def moveZeroesSwap(self, nums: list[int]) -> None:
        k = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1

    # Approach 2: Overwrite Non-Zero Elements
    def moveZeroesOverwrite(self, nums: list[int]) -> None:
        k = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        for i in range(k, len(nums)):
            nums[i] = 0

    # Approach 3: Sorting
    def moveZeroesSort(self, nums: list[int]) -> None:
        nums.sort(key=lambda x: x == 0)


# Testing the approaches
solution = Solution()

nums1 = [0, 1, 0, 3, 12]
solution.moveZeroesSwap(nums1)
print(nums1)

nums2 = [0, 1, 0, 3, 12]
solution.moveZeroesOverwrite(nums2)
print(nums2)

nums3 = [0, 1, 0, 3, 12]
solution.moveZeroesSort(nums3)
print(nums3)
