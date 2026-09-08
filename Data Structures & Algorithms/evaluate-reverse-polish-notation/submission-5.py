class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if(tokens[i]!="*" and tokens[i]!="+" and tokens[i]!="/" and tokens[i]!="-"):
                stack.append(int(tokens[i]))
            else:
                a= stack.pop()
                b= stack.pop()
                print(f"operation: {b} {tokens[i]} {a}")
                if tokens[i]=="+":
                    c = a+b
                elif tokens[i]=="-":
                    c=b-a
                elif tokens[i]=="*":
                    c=a*b
                elif tokens[i]=="/":
                    c=b/a
                stack.append(int(c))
        return int(stack.pop())
        