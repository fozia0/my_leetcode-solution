class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiopQWERTYUIOP")
        row2 = set("asdfghjklASDFGHJKL")
        row3 = set("zxcvbnmZXCVBNM")
    
        result = []
        for word in words:
            if all(c in row1 for c in word) or all(c in row2 for c in word) or all(c in row3 for c in word):
                result.append(word)
        return result
  

