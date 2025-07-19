class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        p = []
        s = [i[0] for i in points]
        s.sort()  
        for j in range(len(s) - 1):
            z = s[j + 1] - s[j]
            p.append(z)
        return max(p)
