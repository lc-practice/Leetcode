# 35 ms	13.8 MB
class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {}
        all_color = []
        num_rod = len(rings)
        for i in range(0,num_rod, 2):
            rods[rings[i+1]] = []
        for i in range(0,num_rod, 2):
            rods[rings[i+1]].append(rings[i])
        for i in rods.keys():
            if len(set(rods[i]))==3:
                all_color.append(i)
        return len(all_color)

# 37 ms	13.8 MB
class Solution:
    def countPoints(self, rings: str) -> int:
        def def_value():
            return []
        rods = defaultdict(def_value)
        all_color = []
        num_rod = len(rings)
        for i in range(0,num_rod, 2):
            rods[rings[i+1]].append(rings[i])
        for i in rods.keys():
            if len(set(rods[i]))==3:
                all_color.append(i)
        return len(all_color)