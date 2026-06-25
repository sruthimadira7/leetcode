"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # initialize boundaries left, right at the both ends of the nums
        left = 0
        right = len(nums)

        # check the condition if left is less than right
        while left < right:
            #  compute mid for each iteration
            mid = (left + right) // 2

            #  check the condition if nums[mid] equals to target or not
            if nums[mid] == target:
                # return mid
                return mid
            # if nums[mid] greater than target 
            # move the right pointer to mid 
            elif nums[mid] > target:
                #  assign mid to right
                right = mid 
            #  else move the left pointer to mid + 1
            else:
                left = mid + 1

        return left



s = Solution()
print(s.searchInsert([1,3,5,6], 5))
print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1,3,5,6], 7))