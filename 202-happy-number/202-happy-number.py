class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set([])
        while n not in visit:
            visit.add(n)
            n = sum(map(lambda x:int(x) ** 2,str(n)))
            if n == 1:
                return True
        return False
        