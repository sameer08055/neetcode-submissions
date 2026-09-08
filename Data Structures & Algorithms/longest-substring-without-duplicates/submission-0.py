class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        charset = set()
        right = 0
        max_max = 0
        while right<len(s):
            while s[right] in charset:
                charset.remove(s[left])
                left = left+1
            charset.add(s[right])
            curr_max = right-left+1
            max_max=max(curr_max,max_max)
            right=right+1
        return max_max

            
            
        