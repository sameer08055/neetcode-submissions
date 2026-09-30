import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        f=[]
        for x,y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(heap,(dist,[x,y]))
        while k>0:
            dis,point = (heapq.heappop(heap))
            k=k-1
            f.append(point)
        return f

        


        