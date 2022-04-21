# 	1034 ms	27.6 MB
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        while j > i:
            max_area = max((j-i)*min(height[i],height[j]),max_area)
            if height[i] > height [j]:
                j -= 1
            else:
                i += 1
        return max_area