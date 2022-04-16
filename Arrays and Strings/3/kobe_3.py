# 64 ms	14 MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else:
            start = 0
            end = 0
            target_string = s[0]
            max_len = 1
            for i in range(1,len(s)):
                if s[i] not in target_string:
                    end = i
                    target_string += s[i]
                    max_len = max(len(target_string),max_len)
                else:
                    while s[i] in s[start: end+1] and start <= end+1:
                        start += 1
                    end = i
                    target_string = s[start: end+1]
        return max_len