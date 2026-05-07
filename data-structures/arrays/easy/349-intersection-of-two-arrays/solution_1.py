"""
349. Intersection Of two Arrays
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
# ─────────────────────────────────────────────────────────────
# APPROACH: Set (Automatic Deduplication)
#
# Core idea:
#   Use a set as the result container — sets automatically
#   reject duplicates, so even if a common element appears
#   multiple times, it is stored only once.
#   Walk through nums1 and add any element that also
#   exists in nums2 to the result set.
#
# Algorithm:
#   1. Initialise an empty result set.
#   2. Iterate over nums1 and check each element against nums2.
#   3. If the element exists in nums2, add it to the result set.
#      Duplicates are silently ignored by the set.
#   4. Convert the result set to a list and return it.
#
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:

        # initialise a set — automatically handles uniqueness
        res = set()

        # iterate over nums1 and check each element against nums2
        for num in nums1:

            # if the element exists in nums2, it's part of the intersection
            if num in nums2:
                res.add(num)   # duplicates are silently ignored by the set

        # convert the result set to a list before returning
        return [num for num in res]


# ── Quick smoke tests ──────────────────────────────────────────
s = Solution()
print(s.intersection([4, 9, 5], [9, 4, 9, 8, 4]))   # Expected: [9, 4]

# ─────────────────────────────────────────────────────────────
# Time Complexity : O(n * m)
#   - Iterating over nums1                   → O(n)
#   - Each `in` check against nums2 (list)   → O(m)
#   - Overall: O(n * m)
#   - Can be improved to O(n + m) by converting
#     nums2 to a set first, making each lookup O(1).
#
# Space Complexity: O(n)
#   - Result set holds at most n unique elements
#     (bounded by the size of nums1).
# ─────────────────────────────────────────────────────────────