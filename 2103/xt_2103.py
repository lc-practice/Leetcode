class Solution:
    def countPoints(self, rings: str) -> int:
        # R, G, B
        count  = [[0, 0, 0] for i in range(10)]
        
        for i in range(0, len(rings), 2):
            rod = int(rings[i+1])

            if rings[i] == 'R':
                count[rod][0] = 1
            elif rings[i] == 'G':
                count[rod][1] = 1
            else:
                count[rod][2] = 1
           
        total = 0
        for i in range(10):
            if sum(count[i]) == 3:
                total += 1
        return total
        
