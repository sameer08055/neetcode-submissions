class Solution:
    def isValid(self, s: str) -> bool:
        matches = {")":"(", "}":"{","]":"["}
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i]=="{" or s[i]=="[":
                stack.append(s[i])
            elif s[i]==")" or s[i]=="}" or s[i]=="]":
                if len(stack)==0 or stack[-1]!=matches[s[i]]:
                    return False
                else:
                    stack.pop()
        return len(stack)==0
            
        