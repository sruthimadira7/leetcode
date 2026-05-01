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
# APPROACH: Simulate Rotation
#
# Core idea:
#   A shift moves the leftmost character to the rightmost position.
#   If we keep shifting s one step at a time, we will cycle through
#   every possible rotation. If any rotation matches goal, return True.
#   After exactly n shifts, s returns to its original form — so we
#   only need to try at most n rotations.
#
# Algorithm:
#   1. Early exit — if lengths differ, no rotation of s can
#      ever equal goal.
#   2. Store the length of s in n — this is the maximum number
#      of rotations we ever need to try.
#   3. Before each shift, check if s already equals goal.
#   4. Perform one shift — move the first character to the end.
#   5. Decrement n and repeat until all rotations are exhausted.
#   6. If no rotation matched, return False.
#
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        # different lengths mean s can never rotate into goal
        if len(s) != len(goal):
            return False

        # at most n rotations before s returns to its original form
        n = len(s)

        while n > 0:

            # check if the current rotation of s matches goal
            if s == goal:
                return True

            # perform one shift — move the leftmost character to the end
            s = s[1:] + s[0]

            # one rotation used up — move closer to the limit
            n -= 1

        return False


# ── Quick smoke tests ──────────────────────────────────────────
s = Solution()
print(s.rotateString("abcde", "cdeab"))   # Expected: True
print(s.rotateString("abcde", "abced"))   # Expected: False

# ─────────────────────────────────────────────────────────────
# Time Complexity : O(n²)
#   - The while loop runs at most n times.
#   - Each string comparison and slice operation costs O(n).
#   - Overall: O(n²).
#
# Space Complexity: O(n)
#   - Each shift creates a new string of length n.
#   - Overall: O(n).
#
# Note — cleaner alternative:
#   Concatenating s with itself (s + s) produces every possible
#   rotation as a substring. Checking if goal is in s + s solves
#   this in a single line: return len(s) == len(goal) and goal in s + s.
# ─────────────────────────────────────────────────────────────