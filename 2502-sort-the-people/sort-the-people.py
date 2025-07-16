class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = dict(zip(heights, names))
        sor = dict(sorted(dic.items(), reverse=True))  
        return list(sor.values())  
           
