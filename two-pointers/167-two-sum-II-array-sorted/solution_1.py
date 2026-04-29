"""
167. Two Sum II - Input Array Is Sorted
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. 
You may not use the same element twice.
Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:
2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""
# ─────────────────────────────────────────────────────────────
# APPROACH: Two Pointers
#
# Core idea:
#   The array is already sorted, so we place one pointer at
#   each end — left at the smallest value, right at the largest.
#   If their sum is too big, we move right inward to get a
#   smaller value. If too small, we move left inward to get a
#   larger value. We keep narrowing until we hit the target.
#
# Algorithm:
#   1. Place left at index 0 (smallest) and right at the
#      last index (largest).
#   2. Compute the sum of numbers[left] + numbers[right].
#   3. If sum equals target — pair found, return their
#      positions incremented by 1 (problem is 1-indexed).
#   4. If sum is too big — decrement right to try a
#      smaller value on the right side.
#   5. If sum is too small — increment left to try a
#      larger value on the left side.
#   6. Repeat until the pair is found.
#
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        # left points to the smallest value, right to the largest
        left = 0
        right = len(numbers) - 1

        while left < right:

            # compute the sum of the current left and right pair
            sum = numbers[left] + numbers[right]

            if sum == target:
                # pair found — add 1 to convert from 0-indexed to 1-indexed
                return [left + 1, right + 1]

            elif sum > target:
                # sum is too big — move right inward to pick a smaller value
                right -= 1

            else:
                # sum is too small — move left inward to pick a larger value
                left += 1

        return []


# ── Quick smoke tests ──────────────────────────────────────────
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))   # Expected: [1, 2]

# ─────────────────────────────────────────────────────────────
# Time Complexity : O(n)
#   - Each iteration moves either left or right by one step.
#   - Together they traverse at most n positions before meeting.
#   - Overall: O(n).
#
# Space Complexity: O(1)
#   - Only two pointer variables are used throughout.
#   - No extra data structures — satisfies the problem's
#     constant space requirement.
# ─────────────────────────────────────────────────────────────