# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。 
# 
#  你可以按任意顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 10⁴ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  只会存在一个有效答案 
#  
# 
#  进阶：你可以想出一个时间复杂度小于 O(n²) 的算法吗？ 
# 
#  Related Topics 数组 哈希表 👍 15369 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 方法一
        # n = len(nums)
        # for i in range(n):
        # for j in range(i+1, n):
        #     if nums[i] + nums[j] == target:
        #         return [i, j]
        # 方法二  使用二分查找 操作无需列表的二分办法
        new_nums = [[num, i] for i, num in enumerate(nums)]
        new_nums.sort(key=lambda i: i[0])
        for i in range(len(new_nums)):
            a = new_nums[i][0]
            b = target - a
            if b > a:
                j = self.binary_search(new_nums, b, i + 1, len(new_nums) - 1)
            else:
                j = self.binary_search(new_nums, b, 0, i - 1)
            if j is not None:
                return [new_nums[i][1], new_nums[j][1]]

    def binary_search(self, li, val, left, right):
        while left <= right:
            mid = (left + right) // 2
            if li[mid][0] == val:
                return mid
            elif li[mid][0] > val:
                right = mid - 1
            else:
                left = mid + 1



# leetcode submit region end(Prohibit modification and deletion)
