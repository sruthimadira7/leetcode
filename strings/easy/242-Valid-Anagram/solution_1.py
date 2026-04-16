"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 10⁴
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters?
How would you adapt your solution to such a case?
"""

# ─────────────────────────────────────────────────────────────
# APPROACH: Sorting
#
# Core idea:
#   Two strings are anagrams if and only if they 
#   contain same characters with same frequencies.

#   Sorting both strings rearranges all characters in alphabetical order, 
#   so two anagrams will always produce identical sorted outputs.
#
# Algorithm:
#   1. Early-exit: if lengths differ, they cannot be anagrams.
#   2. Sort both strings and compare the resulting lists.
#
# Follow-up — Unicode support:
#   This solution already handles Unicode correctly out of the
#   box. Python's sorted() works on any iterable of characters,
#   and Unicode characters are compared by their code points.
#   No changes are needed.
#
# Time Complexity : O(n log n)
#   - Sorting each string of length n costs O(n log n).
#   - The final element-wise comparison of two sorted lists
#     costs O(n).
#   - Overall: O(n log n), dominated by the sort step.
#
# Space Complexity: O(n)
#   - sorted() creates a new list of n characters for each
#     string, so two auxiliary lists of size n are allocated.
#   - Overall: O(n) extra space.
#
# Trade-off vs. hash-map approach:
#   A frequency counter (e.g. collections.Counter) solves this
#   in O(n) time and O(1) space (at most 26 distinct lowercase
#   letters), which is asymptotically faster. The sorting
#   approach is simpler to reason about but slower due to the
#   O(n log n) sort step.
# ─────────────────────────────────────────────────────────────

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # different lengths can never be anagrams
        if len(s) != len(t):
            return False

        # Sort both strings into alphabetical order.
        # sorted() accepts any iterable and returns a new list,
        # leaving the original strings unchanged (immutable).
        # If both sorted lists are equal, every character in s
        # appears in t with the same frequency — i.e. t is an
        # anagram of s.
        return sorted(s) == sorted(t)


# ── Quick smoke tests ──────────────────────────────────────────
s = Solution()
print(s.isAnagram("anagram", "nagaram"))   # Expected: True
print(s.isAnagram("rat", "car"))           # Expected: False