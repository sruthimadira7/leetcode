"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = float("-inf")
        sum = 0

        for num in nums:
            if sum < 0:
                sum = num
            else:
                sum += num
                
            if sum > max_sum:
                max_sum = sum

        return max_sum



s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))