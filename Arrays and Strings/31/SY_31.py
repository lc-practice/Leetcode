class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        # i == 0 means the number is in 654321 order and the next permutation will just be everything reversed
        if i == 0:
            return nums.reverse()
        
        # if i != 0, we find the next larger number than nums[i-1]
        j = i
        while j < n and nums[j] > nums[i-1]:
            j += 1
        
        # swap position of nums[i-1] and nums[j-1], since nums[j-1] will be the next larger number than nums[i] among all
        nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
        
        # since from i to the end, all numbers are in descending order. Make them ascending for the next permutation
        nums[i:] =  reversed(nums[i:])
        
        return