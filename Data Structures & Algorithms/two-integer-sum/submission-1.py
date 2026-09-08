class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i, num in enumerate(nums):
            j = target - num
            if j in count:
                return[count[j],i]
            count[num]=i
        return []


