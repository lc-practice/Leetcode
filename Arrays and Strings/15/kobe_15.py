# 7255 ms	18.2 MB
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_list = []
        for i in range(len(nums)-2):
            anchor = nums[i]
            rest = nums[i+1:]
            rest.sort()
            rest_left = 0
            rest_right = len(rest) - 1
            while rest_left < rest_right:
                if rest[rest_left]+rest[rest_right]+anchor == 0:
                    sub_list = [rest[rest_left], rest[rest_right], anchor]
                    sub_list.sort()
                    if sub_list not in result_list:
                        result_list.append(sub_list)
                if rest[rest_left]+rest[rest_right] < -anchor:
                    rest_left += 1
                else:
                    rest_right -= 1
        return result_list