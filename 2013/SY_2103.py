class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        # each element is a dictionary that records 
        rods = [collections.Counter() for _ in range(10)]
        
        for i in range(0, n, 2):
            # print(i)
            color = rings[i]
            rod_ind = int(rings[i+1])
            rods[rod_ind][color] |= 1
        rods = [len(d) == 3 for d in rods]
        return(sum(rods))