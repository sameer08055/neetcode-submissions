class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        most_water = 0
        while left<right:
            water = min(heights[left],heights[right])*(right-left)
            if(water>most_water):
                most_water = water
            if(heights[left]>heights[right]):
                right = right-1
            elif(heights[left]<heights[right]):
                left = left+1
            else:
                left = left+1
        return most_water
        