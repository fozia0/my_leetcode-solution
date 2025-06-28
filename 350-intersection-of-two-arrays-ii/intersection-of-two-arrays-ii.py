class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = []                      
        n = len(nums1)
        m = len(nums2)
        used = [False] * m          
        for i in range(n):          
            for j in range(m):      
                if not used[j] and nums1[i] == nums2[j]:
                    s.append(nums1[i])   
                    used[j] = True       
                    break                

        return s                         
