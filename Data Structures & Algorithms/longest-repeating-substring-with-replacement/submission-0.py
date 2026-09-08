class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        charmap = {}
        max_len=0
        while right < len(s):
            charmap[s[right]] = charmap.get(s[right], 0) + 1
            window_size=right-left+1
            char_to_replace = window_size - max(charmap.values())
            if char_to_replace <= k:
                max_len=max(max_len,window_size)
            else:
                charmap[s[left]]=charmap[s[left]]-1
                left=left+1
            right = right+1
        return max_len
            
        
        