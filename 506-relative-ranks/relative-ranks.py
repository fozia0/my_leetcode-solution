class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        original = score.copy()
        sorted_score = sorted(score, reverse=True)
        rank = {}
        for i in range(len(sorted_score)):
            if i == 0:
                rank[sorted_score[i]] = "Gold Medal"
            elif i == 1:
                rank[sorted_score[i]] = "Silver Medal"
            elif i == 2:
                rank[sorted_score[i]] = "Bronze Medal"
            else:
                rank[sorted_score[i]] = str(i + 1)
        result = [rank[s] for s in original]
        return result

        