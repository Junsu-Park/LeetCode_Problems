import heapq

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, s in enumerate(score):
            heapq.heappush(heap, [-s[k], i])

        ans = []
        for j in range(len(heap)):
            tmp_max = heapq.heappop(heap)
            ans.append(score[tmp_max[1]])
        
        return ans
        