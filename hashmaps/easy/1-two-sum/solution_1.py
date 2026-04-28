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
2 <= nums.length <= 10⁴
-10⁹ <= nums[i] <= 10⁹
-10⁹ <= target <= 10⁹
Only one valid answer exists.

Follow up: Can you come up with an algorithm that is less than O(n²) time complexity?
"""
# ─────────────────────────────────────────────────────────────
# APPROACH: Brute Force (Nested Loops)
#
# Core idea:
#   Try every possible pair of indices (i, j) where j > i.
#   If the two numbers at those indices sum to the target,
#   return their indices immediately.
#
# Algorithm:
#   1. Store the length of nums to avoid repeated len() calls.
#   2. Phase 1 — outer loop iterates over each index i from 0 to n-1.
#   3. Phase 2 — inner loop iterates over each index j from i+1 to n-1,
#      ensuring each pair is checked exactly once.
#   4. If nums[i] + nums[j] equals target, return [i, j].
#   5. If no pair is found after all iterations, return empty list.
#
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # store the length of the given list
        n = len(nums)

        # iterate the list using two nested loops
        for i in range(n - 1):

            # j starts from i+1 to avoid duplicates and self-pairing
            for j in range(i + 1, n):

                # check if the two numbers at indices i and j sum to target
                if nums[i] + nums[j] == target:

                    # pair found — return their indices
                    return [i, j]

        return []


# ── Quick smoke tests ──────────────────────────────────────────
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))   # Expected: [0, 1]
print(s.twoSum([3, 2, 4], 6))        # Expected: [1, 2]
print(s.twoSum([3, 3], 6))           # Expected: [0, 1]

# ─────────────────────────────────────────────────────────────
# Time Complexity : O(n²)
#   - Outer loop iterates over n elements            → O(n)
#   - Inner loop iterates over up to n-1 elements    → O(n)
#   - Combined: O(n²) — every pair is checked once.
#   - Total pairs checked: n(n-1)/2
#
# Space Complexity: O(1)
#   - No extra data structures used.
#   - Only a constant number of variables (n, i, j).
#   - Output list [i, j] is not counted as extra space.
#
# Follow-up — Can we do better than O(n²)?
#   Yes — using a Hash Map we can solve this in O(n) time
#   and O(n) space by storing each number's index as we
#   iterate, then checking if the complement (target - num)
#   already exists in the map.
# ─────────────────────────────────────────────────────────────