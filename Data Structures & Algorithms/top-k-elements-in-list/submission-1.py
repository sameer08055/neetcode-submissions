import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for i in nums:
            map[i]=map.get(i,0)+1
        min_heap=[]
        for (key,value) in map.items():
            heapq.heappush(min_heap,(value,key))
            if(len(min_heap)>k):
                heapq.heappop(min_heap)
        return [t[1] for t in min_heap]
        