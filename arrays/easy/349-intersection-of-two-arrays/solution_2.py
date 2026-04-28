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
# APPROACH: Set Lookup
#
# Core idea:
#   Convert nums1 into a set to eliminate duplicates and
#   enable O(1) lookups. Then walk through nums2 — every
#   element that exists in the set belongs to the intersection.
#
# Algorithm:
#   1. Initialise an empty result list.
#   2. Convert nums1 to a set — removes duplicates and
#      makes every membership check O(1).
#   3. Iterate over nums2 and check each element
#      against nums1_set.
#   4. If it exists in nums1_set, append it to the result.
#   5. Return the result list.
#
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:

        # initialise an empty list to store the intersection elements
        res = []

        # convert nums1 to a set — removes duplicates, O(1) lookups
        nums1_set = set(nums1)

        # iterate over nums2 and check each element against nums1_set
        for num in nums2:

            # if the element exists in nums1_set, it's part of the intersection
            if num in nums1_set:
                res.append(num)

        return res


# ── Quick smoke tests ──────────────────────────────────────────
s = Solution()
print(s.intersection([4, 9, 5], [9, 4, 9, 8, 4]))   # Expected: [9, 4]

# ─────────────────────────────────────────────────────────────
# Time Complexity : O(n + m)
#   - Converting nums1 to a set              → O(n)
#   - Iterating over nums2                   → O(m)
#   - Each `in` check against nums1_set      → O(1) avg
#   - Overall: O(n + m)
#
# Space Complexity: O(n)
#   - nums1_set holds at most n unique elements.
#   - Result list holds at most min(n, m) elements.
#
# Note — duplicate elements in result:
#   If nums2 contains duplicates (e.g. [9,4,9,8,4]),
#   the result may contain duplicates too (e.g. [9,4,9,4]).
#   To guarantee unique results, wrap res in a set()
#   or add a `res_set` check before appending.
# ─────────────────────────────────────────────────────────────