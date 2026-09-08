class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_max = 0
        charset = set()
        while right < len(s):
            while s[right] in charset:
                charset.remove(s[left])
                left=left+1
            charset.add(s[right])
            right=right+1
            curr_max = right-left
            max_max=max(curr_max,max_max)
        return max_max
        