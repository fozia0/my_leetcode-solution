class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(str(digit)for digit in digits))
        num +=1
        new = [int(d) for d in str(num)]
        return new
