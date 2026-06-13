"""
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:
Input: s = "f11", t = "b23"
Output: false

Explanation:
The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
# ─────────────────────────────────────────────────────────────
# APPROACH: Brute-Force (Pairwise Map Scan)
#
# Core idea:
#   Two strings are isomorphic if there exists a strict one-to-one
#   mapping between their characters — every s[i] always maps to
#   the same t[i], and no two different s-characters map to the
#   same t-character. We build the mapping incrementally and
#   before each insertion we scan the existing map to detect
#   either of the two violation types.
#
# Two violation types that break isomorphism:
#   Type 1 — many-to-one: a different s-char already maps to t[i]
#             e.g. s_counter has 'g' → 'd', now 'x' wants → 'd'
#             detected by: val == t[i] and key != s[i]
#   Type 2 — one-to-many: s[i] is already mapped to a different t-char
#             e.g. s_counter has 'g' → 'd', now 'g' wants → 'z'
#             detected by: key == s[i] and val != t[i]
#
# Algorithm:
#   1. Early-exit if len(s) != len(t) — unequal lengths can never
#      be isomorphic.
#   2. Iterate index i from 0 to n-1:
#        a. Scan every (key, val) pair in s_counter.
#        b. If either violation type is found, return False.
#        c. Record the mapping s_counter[s[i]] = t[i].
#   3. If no violation was found across all positions, return True.
#
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):      # unequal lengths → can never be isomorphic
            return False

        n = len(s)
        s_counter = {}             # maps each s-character to its t-character

        for i in range(n):

            # scan all existing mappings before recording s[i] → t[i]
            for key, val in s_counter.items():

                # Type 1 — many-to-one violation:
                #   a different s-char already claims t[i] as its target
                # Type 2 — one-to-many violation:
                #   s[i] is already mapped but to a different t-char
                if val == t[i] and key != s[i] or val != t[i] and key == s[i]:
                    return False

            s_counter[s[i]] = t[i]     # safe to record — no violation found at position i

        return True     # all positions passed both violation checks


# ── Quick smoke tests ──────────────────────────────────────────
s = Solution()
print(s.isIsomorphic("egg", "add"))            # Expected: True
print(s.isIsomorphic("paper", "title"))        # Expected: True
print(s.isIsomorphic("paperssss", "titlesese")) # Expected: False
print(s.isIsomorphic("f11", "a23"))            # Expected: False

# Note — why scan the whole map instead of just checking s_counter.get(s[i])?
#   s_counter.get(s[i]) catches Type 2 (one-to-many) instantly.
#   But Type 1 (many-to-one) requires knowing whether t[i] is already
#   someone else's target — which needs a full scan of values.
#   A second reverse map (t_char → s_char) would catch both in O(1),
#   making the overall solution O(n) instead of O(n²). See below.
#
# Optimised alternative — two hash maps (O(n)):
#   s_to_t = {}    # s-char → t-char
#   t_to_s = {}    # t-char → s-char
#   for sc, tc in zip(s, t):
#       if s_to_t.get(sc, tc) != tc or t_to_s.get(tc, sc) != sc:
#           return False
#       s_to_t[sc] = tc
#       t_to_s[tc] = sc
#   return True
#
# problem: 205-isomorphic-strings
#
# Time Complexity : O(n²)
#   - The outer loop runs n times                              → O(n)
#   - The inner scan iterates over s_counter, which grows
#     up to k distinct characters (k ≤ 26 for ASCII letters)  → O(k)
#   - In the worst case k = n (all unique chars), making
#     the inner scan O(n) per outer step                       → O(n²)
#   - Overall: O(n²) worst case.
#
# Space Complexity: O(k)
#   - s_counter holds at most k distinct s-characters          → O(k)
#   - For lowercase ASCII letters k ≤ 26                      → O(1)
#   - Overall: O(k), effectively O(1) for fixed alphabets.
# ─────────────────────────────────────────────────────────────