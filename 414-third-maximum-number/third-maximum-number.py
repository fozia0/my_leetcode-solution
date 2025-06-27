class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sort = sorted(set(nums), reverse=True)
        n = len(sort)        
        if n >= 3:      
            return sort[2] 
        else:
            return sort[0]

        