class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        for row in score:
            score.sort(key=lambda row:row[k],reverse=True)
        return score
        