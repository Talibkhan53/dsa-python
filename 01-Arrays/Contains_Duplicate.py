class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
      store = {}
      if len(nums) < 2:
        return False
      for index,value in enumerate(nums):
        if value in store:
            return True
        store[value] = index
      return False
    

        
        
