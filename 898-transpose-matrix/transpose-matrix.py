class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        z = zip(*matrix)
        return [list(i) for i in z]
