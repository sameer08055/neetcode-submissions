class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = {}
        for c in s1:
            s1map[c]=s1map.get(c,0)+1
        s2map = {}
        left=0
        right=0
        while right < len(s2):
            s2map[s2[right]]=s2map.get(s2[right],0)+1
            if right-left+1>len(s1):
                s2map[s2[left]]=s2map[s2[left]]-1
                if s2map[s2[left]] == 0:
                    del s2map[s2[left]]
                left=left+1
            if right-left+1 == len(s1):
                if(s1map==s2map):
                    return True
            right = right+1
        return False

            

        
        