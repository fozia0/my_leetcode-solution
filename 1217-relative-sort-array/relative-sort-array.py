class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = []
        non = []
        for i in arr2:
            for j in arr1:
                if j == i:
                    arr.append(j)
        for k in arr1:
            if k not in arr2:
                non.append(k) 
                non.sort()
        arr.extend(non)
        return arr 
        