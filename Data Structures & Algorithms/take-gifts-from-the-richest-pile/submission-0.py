import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-gifts for gifts in gifts]
        heapq.heapify(maxHeap)
        while k>0:
            a = heapq.heappop(maxHeap)
            a = abs(a)
            b = math.floor(math.sqrt(a))
            heapq.heappush(maxHeap,-b)
            k = k-1
        return -1*sum(maxHeap)
        


        