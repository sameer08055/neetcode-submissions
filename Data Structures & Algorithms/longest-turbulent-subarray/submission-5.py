class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l,r = 0,1
        prev = ""
        res = 1
        while r<len(arr):
            if(arr[r]>arr[r-1] and prev!=">"):
                res = max(res,r-l+1) 
                prev=">"
                r=r+1
            elif(arr[r]<arr[r-1] and prev!="<"):
                res = max(res,r-l+1)
                prev="<"
                r=r+1
            else:
                if(arr[r]==arr[r-1]):
                    l=r
                    r+=1
                    prev=""
                else:
                    l=r-1
                    prev=""
        return res

                


                

        