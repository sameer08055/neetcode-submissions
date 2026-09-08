class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        current = 0
        largest = 0
        while left < right:
            current = min(heights[left],heights[right])*(right-left)
            largest = max(current,largest)
            if(heights[left]<heights[right]):
                left = left+1
            elif(heights[left]>heights[right]):
                right = right-1
            else:
                left = left+1
        return largest


            
        