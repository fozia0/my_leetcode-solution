class Solution:
    def sortSentence(self, s: str) -> str:
        rev = []
        result = []
        for i in s.split():
            rev.append(i[::-1])
        rev.sort()
        rev = [j[1:] for j in rev]

        for i in rev:
            result.append(i[::-1])
        return ' '.join(result)