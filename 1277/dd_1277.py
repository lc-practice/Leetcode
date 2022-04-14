# problem link: https://leetcode.com/problems/count-square-submatrices-with-all-ones/
# Solution time: 20 mins
# Runtime: 1228 ms, faster than 9.85% of Python3 online submissions for Count Square Submatrices with All Ones.
# Memory Usage: 16.3 MB, less than 37.75% of Python3 online submissions for Count Square Submatrices with All Ones.

class Solution:
    def countSquares(self, matrix) -> int:
        total_num_square = 0

        # check edge case when there is no element and return 0
        if len(matrix) == 0:
            return total_num_square

        # set slide upper bound - max of (m, n)
        m_length = len(matrix)
        n_length = len(matrix[0])
        max_slide = min(m_length, n_length)

        for m in range(m_length):
            for n in range(n_length):
                point = matrix[m][n]
                print(f"point - {point} with m {m} and n {n}")
                for slide in range(1, max_slide + 1):
                    ## Checking if m + slide will exceed the n_length if yes the break
                    if m + slide > m_length or n + slide > n_length:
                        continue
                    expected_slide_sum = (slide) * (slide)
                    slide_sum = sum([matrix[m_][n_] for m_ in range(m, m+slide) for n_ in range(n, n+slide)])
                    if expected_slide_sum == slide_sum:

                        total_num_square += 1
                    else:
                        break

        return total_num_square
