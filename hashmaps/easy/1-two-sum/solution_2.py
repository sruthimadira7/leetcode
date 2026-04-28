"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
# ─────────────────────────────────────────────────────────────
# APPROACH: Hash Map (Complement Lookup)
#
# Core idea:
#   For every number in nums, its required partner is
#   target - nums[i] (the complement / difference).
#   Instead of searching the entire array for that partner
#   with a second loop, we store each number and its index
#   in a hash map as we go — turning the lookup into O(1).
#
# Algorithm:
#   1. Initialise an empty diff_map to store each number
#      and its index as we iterate.
#   2. For each index i, compute diff = target - nums[i].
#   3. If diff already exists in diff_map, we found the pair —
#      return [diff_map[diff], i].
#   4. Otherwise, store nums[i] → i in diff_map and move on.
#   5. If no pair is found after all iterations, return [].
#
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # initialise a diff_map to store each number
        # and its respective index as we iterate
        diff_map = {}

        # store the length of the given list
        n = len(nums)

        # iterate the given list
        for i in range(n):

            # calculate the complement needed to reach target
            diff = target - nums[i]

            # if the complement was seen before, we have our pair
            if diff in diff_map:

                # return the stored index of diff and the current index
                return [diff_map[diff], i]

            # complement not found yet — store current number and its index
            diff_map[nums[i]] = i

        return []


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))   # Expected: [0, 1]

# ─────────────────────────────────────────────────────────────
# Time Complexity : O(n)
#   - Single loop iterates over n elements           → O(n)
#   - Each dict lookup / insert is O(1) avg.
#   - Overall: O(n), a strict improvement over the O(n²)
#     brute force nested loop approach.
#
# Space Complexity: O(n)
#   - diff_map stores at most n key-value pairs.
#   - In the worst case (pair found at the last two elements),
#     the map grows to hold n-1 entries.
# ─────────────────────────────────────────────────────────────