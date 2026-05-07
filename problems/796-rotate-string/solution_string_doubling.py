"""
796. Rotate String

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.

Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:
Input: s = "abcde", goal = "abced"
Output: false

Constraints:
1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.
"""
# ─────────────────────────────────────────────────────────────
# APPROACH: Doubled String + Substring Search
#
# Core idea:
#   Every possible rotation of s appears as a substring inside
#   s + s. For example, "abcde" doubled is "abcdeabcde", which
#   contains every rotation — "bcdea", "cdeab", "deabc" and so on.
#   So instead of simulating each rotation one by one, we just
#   double s and check if goal appears anywhere inside it.
#
# Algorithm:
#   1. Early exit — if lengths differ, no rotation can match.
#   2. Double s to produce a string that contains every possible
#      rotation of s as a substring.
#   3. Use Python's `in` operator to check if goal exists anywhere
#      inside doubled_s — if it does, s can rotate into goal.
#
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        # different lengths mean s can never rotate into goal
        if len(s) != len(goal):
            return False

        # doubling s produces a string that contains every possible rotation
        doubled_s = s * 2

        # if goal appears anywhere in doubled_s, it is a valid rotation of s
        return goal in doubled_s


# ── Quick smoke tests ──────────────────────────────────────────
s = Solution()
print(s.rotateString("abcde", "cdeab"))   # Expected: True
print(s.rotateString("abcde", "abced"))   # Expected: False

# ─────────────────────────────────────────────────────────────
# Time Complexity : O(n)
#   - Doubling s costs O(n).
#   - Python's `in` operator uses an optimised internal search
#     algorithm that runs in O(n) on average.
#   - Overall: O(n).
#
# Space Complexity: O(n)
#   - doubled_s is a new string of length 2n.
#   - Overall: O(n).
# ─────────────────────────────────────────────────────────────