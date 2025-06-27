class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority = set()
        count = {}

        for i in nums:                    
            count[i] = count.get(i, 0) + 1
            if count[i] > n // 2:         
                majority.add(i)
                return majority.pop()       


        

        