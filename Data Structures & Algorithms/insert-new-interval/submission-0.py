class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = intervals.copy()
        result.append(newInterval)
        result.sort(key = lambda x:x[0])
        final_result = [result[0]]
        for i in range(1,len(result)):
            if(result[i][0]<=final_result[-1][1]):
                final_result[-1][1]=max(result[i][1],final_result[-1][1])
            else:
                final_result.append(result[i])
        return final_result
