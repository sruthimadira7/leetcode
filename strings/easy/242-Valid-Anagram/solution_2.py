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
#   We record the frequency of each character in s, then
#   "consume" those counts while walking through t. If any
#   character in t is missing from the map or has been fully
#   consumed (count == 0), the strings are not anagrams.
#
# Algorithm:
#   1. Early-exit: if lengths differ, they cannot be anagrams.
#   2. Phase 1 — build a frequency map by iterating over s.
#   3. Phase 2 — iterate over t, decrementing counts; return
#      False the moment a character is absent or exhausted.
#   4. If Phase 2 completes without returning False, every
#      character balanced out → return True.
#
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

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # different lengths can never be anagrams
        if len(s) != len(t):
            return False

        # freq_map[ch] = number of times ch still needs to be
        # matched by t. Starts populated from s, then drained
        # by t in Phase 2.
        freq_map = {}

        # ── Phase 1: Build frequency map from s ───────────────
        for ch in s:
            # dict.get(key, default) safely returns 0 for keys
            # that haven't been seen yet, avoiding a KeyError.
            freq_map[ch] = freq_map.get(ch, 0) + 1

        # ── Phase 2: Verify t against the frequency map ───────
        for ch in t:
            # Case A — ch never appeared in s at all.
            # Case B — ch appeared in s but has already been
            #          fully consumed (count reached 0), meaning
            #          t contains more occurrences than s does.
            # Either case disqualifies an anagram relationship.
            if ch not in freq_map or freq_map[ch] == 0:
                return False

            # ch is present and still has remaining count.
            # Consume one occurrence; if t is a true anagram
            # every count will reach exactly 0 by the end.
            freq_map[ch] -= 1

        # Every character in t found a matching, unconsumed
        # character in s. Since lengths are equal (checked
        # upfront), all counts are now exactly 0 → valid anagram.
        return True


# ── Quick smoke tests ──────────────────────────────────────────
s = Solution()
print(s.isAnagram("anagram", "nagaram"))   # Expected: True
print(s.isAnagram("rat", "car"))           # Expected: False