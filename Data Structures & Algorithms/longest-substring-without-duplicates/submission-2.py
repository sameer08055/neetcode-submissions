class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        window = set()
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left = left+1
                pass
            window.add(s[right])
            if(len(window)>longest):
                longest = len(window)
            pass
        return longest
        