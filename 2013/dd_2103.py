# problem link: https://leetcode.com/problems/rings-and-rods/
# Solution time: 5 mins
# Runtime: 34 ms, faster than 76.73% of Python3 online submissions for Rings and Rods.
# Memory Usage: 13.8 MB, less than 97.82% of Python3 online submissions for Rings and Rods.

class Solution:
    def countPoints(self, rings: str) -> int:
        rod_dict = {}
        
        for i in range(0, len(rings), 2):   
            color = rings[i]
            rod   = rings[i+1]
            
            rod_dict[rod] = rod_dict.get(rod, set())
            rod_dict[rod].add(color)
        
        result = 0
        for k, v in rod_dict.items():
            if len(v)>=3:
                result+= 1
                
        return result