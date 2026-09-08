class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        glmax,glmin = nums[0],nums[0]
        curmax,curmin = 0,0
        total = 0
        for n in nums:
            curmax = max(curmax+n, n)
            curmin = min(curmin+n, n)
            total = total+n
            glmax = max(glmax, curmax)
            glmin=min(glmin, curmin)
        if(glmax>0):
            return max(glmax,total-glmin)
        else:
            return glmax
        