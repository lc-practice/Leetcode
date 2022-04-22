class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        # print(nums)
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums)-1
            
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                
                if temp > 0:
                    right -= 1
                
                elif temp < 0:
                    left += 1
                
                else:
                    out.append([nums[i], nums[left], nums[right]])
                    # print([temp, i, left, right])
                    # remove repetitive cases
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1
                
        return out