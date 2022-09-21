#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for li in matrix:
        #     if target in li:
        #         return True
        # return False
        if not matrix:  # 考虑边界效应
            return False
        h = len(matrix)
        w = len(matrix[0])
        if not w:  # 考虑边界效应
            return False
        right = h * w - 1
        left = 0
        while left <= right:
            mid = (left+right) // 2
            i = mid // w
            j = mid % w
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
# @lc code=end
