class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = 0
        curr_count = 0
        for i in range(0,len(nums)):
            if(nums[i]==1):
                curr_count = curr_count+1
            else:
                curr_count = 0
            maxcount = max(maxcount,curr_count)
        return maxcount
        