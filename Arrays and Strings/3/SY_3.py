'''
This is slow though...
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0 # counter for the length of longest substring
        for i, c in enumerate(s):
            indices = {} # dictionary to store the starting index of a character
            r = i + 1
            indices[c] = i
            while r < len(s) and (s[r] not in indices or indices[s[r]] >= r):
                indices[s[r]] = r
                r += 1
            # update the counter
            count = max(count, r - i)
            del indices
        return count


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0 # counter for the length of longest substring
        visited = {} # dictionary to keep track of the position for the most recently-visted character
        start = 0 # index of the starting character in the longest substring
        for i, c in enumerate(s):
            # if c is visited before and this c is at or after the position of the starting character
            #   reset the index of the startinc character to the next one    
            if c in visited and visited[c] >= start:
                start = visited[c] + 1
            else:
            # if not visited before or the character we previously visited is before the "start" we don't care
                count = max(count, i - start + 1)
            visited[c] = i # always update the index!!!
        return count