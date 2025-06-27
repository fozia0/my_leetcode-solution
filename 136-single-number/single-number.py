class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = set()
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                single.add(nums[i])
                return single.pop()


        