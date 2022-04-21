class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                for output in self.twoSum(nums, i + 1, 0 - nums[i]):
                    res.append([nums[i]] + output)
        return res
    
    def twoSum(self, nums, start, target):
        result = []
        s = set()
        for i in range(start, len(nums)):
            if len(result) == 0 or result[-1][1] != nums[i]:
                complement = target - nums[i]
                if complement in s:
                    result.append([complement, nums[i]])
                s.add(nums[i])
        return result
