class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_value = set(nums)
        for i in range(len(nums) + 1):
            if i not in missing_value:
                return i
                
        