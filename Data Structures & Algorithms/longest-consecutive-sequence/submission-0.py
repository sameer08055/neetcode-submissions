class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longest = 0
        for num in nums:
            if num-1 not in nums:
                start = num
                current =1
                while start+1 in nums:
                    start = start+1
                    current = current +1
                longest = max(current,longest)
        return longest


        


        