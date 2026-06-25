"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        print(nums)

        # initialize left and right pointers at both ends of the array
        left = 0
        right = len(nums) - 1

        while left <= right:
            # compute mid for each iteration
            mid = (left + right) // 2

            if nums[mid] == target:
                # target found, return the index
                return mid
            elif nums[mid] > target:
                # target is in the left half, move right pointer
                right = mid - 1
            else:
                # target is in the right half, move left pointer
                left = mid + 1

        # target not found
        return -1

s = Solution()
print(s.search([-1,0,3,5,9,12], 9))
print(s.search([-1,0,3,5,9,12], 2))