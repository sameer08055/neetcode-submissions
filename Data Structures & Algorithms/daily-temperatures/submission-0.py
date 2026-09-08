class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        output_array=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while len(stack)!= 0 and temperatures[i]>temperatures[stack[-1]]:
                p = stack.pop()
                output_array[p]=i-p
            stack.append(i)
        return output_array


        