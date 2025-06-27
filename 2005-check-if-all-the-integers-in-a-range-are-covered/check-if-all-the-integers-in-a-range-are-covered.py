class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        numbers = set()
        for start, end in ranges:
            for i in range(start, end + 1):
                numbers.add(i)

        for i in range(left, right + 1):
            if i not in numbers:
                return False
        return True

    
