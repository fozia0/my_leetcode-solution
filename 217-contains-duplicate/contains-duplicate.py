class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        value = set()               
        for i in nums:           
            if i in value:        
                return True        
            value.add(i)          
        return False               

                   