class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            mat = [list(i) for i in zip(*mat[::-1])]
            if mat == target:
                return True
        return False
            