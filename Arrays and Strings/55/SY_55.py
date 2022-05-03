# This is slow
class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        i = n - 2
        nums[-1] = True
        while i >= 0:
            if nums[i] >= n - i - 1:
                nums[i] = True
            elif nums[i] == 0:
                nums[i] = False
            else:
                nums[i] = True if max(nums[i+1 : i+nums[i]+1]) == True else False
            i -= 1
        return nums[0]
            
    # Optimal
    class Solution:
        def canJump(self, nums) -> bool:
            n = len(nums)
            last = n - 1
            i = n - 2
            while i >= 0:
                if nums[i] + i >= last:
                    last = i
                i -= 1
            return last == 0