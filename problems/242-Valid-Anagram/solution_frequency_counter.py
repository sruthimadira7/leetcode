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
#   We record the frequency of each character in s,
#   then walk through t — decrementing each count.
#   If every count reaches zero, both strings are anagrams.
#
# Algorithm:
#   1. Early exit — if lengths differ, they cannot be anagrams.
#   2. Phase 1 — build a frequency map by iterating over s,
#      counting how many times each character appears.
#   3. Phase 2 — iterate over t, decrementing each character's
#      count. Return False the moment a character is absent
#      or its count has already reached zero.
#   4. If Phase 2 completes without returning False, every
#      character balanced out → return True.
#
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # unequal lengths mean the strings can never be anagrams
        if len(s) != len(t):
            return False

        # initialise a frequency map to store each character
        # and the number of times it appears in s
        s_char_freq = {}

        # Phase 1 — build frequency map from s
        for ch in s:
            # increment count for ch, defaulting to 0 on first encounter
            s_char_freq[ch] = s_char_freq.get(ch, 0) + 1

        # Phase 2 — verify t against the frequency map
        for ch in t:
            # ch is either not in s at all, or already fully consumed
            # either way t cannot be an anagram of s
            if ch not in s_char_freq or s_char_freq[ch] == 0:
                return False

            # character matched — consume one occurrence
            s_char_freq[ch] -= 1

        return True


# ── Quick smoke tests ──────────────────────────────────────────
s = Solution()
print(s.isAnagram("anagram", "nagaram"))   # Expected: True
print(s.isAnagram("rat", "car"))           # Expected: False

# ─────────────────────────────────────────────────────────────
# Follow-up — Unicode support:
#   This solution handles Unicode automatically. Python dicts
#   accept any hashable key, so Unicode characters are stored
#   just like ASCII ones. No changes are needed.
#
# Time Complexity : O(n)
#   - Phase 1 iterates over s once           → O(n)
#   - Phase 2 iterates over t once           → O(n)
#   - Each dict lookup / update is O(1) avg.
#   - Overall: O(n), a strict improvement over the O(n log n)
#     sorting approach.
#
# Space Complexity: O(k)  ≈  O(1) for lowercase-only input
#   - The frequency map holds at most k distinct characters,
#     where k is the size of the alphabet.
#   - For the constrained input (lowercase a–z), k ≤ 26, so
#     space is effectively O(1) — constant regardless of n.
#   - For arbitrary Unicode, k can grow up to O(n) in the
#     worst case (all characters distinct).
# ─────────────────────────────────────────────────────────────