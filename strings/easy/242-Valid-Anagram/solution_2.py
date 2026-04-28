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
# APPROACH: Hash Map (Frequency Counter)
#
# Core idea:
#   Two strings are anagrams if and only if every character
#   appears the same number of times in both strings.
#   We build a frequency map for each string independently,
#   then compare the two maps for equality.
#
# Algorithm:
#   1. Define a helper char_count(s) that iterates over a
#      string and returns a dict mapping each character
#      to the number of times it appears.
#   2. Call char_count on both s and t.
#   3. If the two dicts are equal, every character matches
#      in frequency → return True, otherwise False.
#
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def char_count(s: str):
            s_counter = {}
            for ch in s:
                if ch not in s_counter:
                    s_counter[ch] = 0     # initialise key on first encounter

                s_counter[ch] += 1        # increment frequency

            return s_counter

        # Equal dicts means identical character frequencies → anagram
        return char_count(s) == char_count(t)


# ── Quick smoke tests ──────────────────────────────────────────
s = Solution()
print(s.isAnagram("anagram", "nagaram"))   # Expected: True
print(s.isAnagram("rat", "car"))           # Expected: False

# Follow-up — Unicode support:
#   This solution handles Unicode automatically. Python dicts
#   accept any hashable key, so Unicode characters are stored
#   just like ASCII ones. No changes are needed.
#
# Time Complexity : O(n)
#   - char_count(s) iterates over s once     → O(n)
#   - char_count(t) iterates over t once     → O(n)
#   - Each dict lookup / update is O(1) avg.
#   - Overall: O(n), a strict improvement over the O(n log n)
#     sorting approach.
#
# Space Complexity: O(k)  ≈  O(1) for lowercase-only input
#   - Each frequency map holds at most k distinct characters,
#     where k is the size of the alphabet.
#   - For the constrained input (lowercase a–z), k ≤ 26, so
#     space is effectively O(1) — constant regardless of n.
#   - For arbitrary Unicode, k can grow up to O(n) in the
#     worst case (all characters distinct).
# ─────────────────────────────────────────────────────────────