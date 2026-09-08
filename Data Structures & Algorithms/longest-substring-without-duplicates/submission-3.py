class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        longest = 0
        for right in range(0,len(s)):
            while s[right] in window:
                window.remove(s[left])
                left = left+1
            window.add(s[right])
            if(len(window)>longest):
                longest = len(window)
        return longest

        