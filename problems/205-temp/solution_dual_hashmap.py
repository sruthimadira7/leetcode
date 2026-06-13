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
# APPROACH: Optimised Two Hash Maps
#
# Core idea:
#   Two strings are isomorphic if there is a strict one-to-one
#   mapping between their characters — every s[i] always maps
#   to the same t[i], and no two different s-characters map to
#   the same t-character. Maintaining two maps simultaneously
#   catches both violation types in O(1) per position:
#
# Two violation types that break isomorphism:
#   Type 1 — one-to-many : s[i] is already mapped to a different t-char
#             e.g. s_map_t has 'g' → 'd', now 'g' is seen with 'z'
#             detected by: s_map_t[s[i]] != t[i]
#   Type 2 — many-to-one : t[i] is already someone else's target
#             e.g. t_map_s has 'd' → 'g', now 'x' wants → 'd'
#             detected by: t[i] in t_map_s (when s[i] is new)
#
# Algorithm:
#   1. Early-exit if len(s) != len(t) — unequal lengths can
#      never be isomorphic.
#   2. Iterate index i from 0 to n-1:
#        a. If s[i] is new to s_map_t:
#             - Check Type 2: if t[i] is already in t_map_s,
#               another s-char owns it → return False.
#             - Otherwise record both directions:
#               s_map_t[s[i]] = t[i] and t_map_s[t[i]] = s[i].
#        b. Check Type 1: if s_map_t[s[i]] != t[i], the existing
#           mapping conflicts with the current position → return False.
#   3. If no violation found, return True.
#
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):      # unequal lengths → can never be isomorphic
            return False

        n = len(s)
        s_map_t = {}     # forward map  : s-char → t-char
        t_map_s = {}     # reverse map  : t-char → s-char

        for i in range(n):

            if s[i] not in s_map_t:     # s[i] is seen for the first time

                # Type 2 — many-to-one violation:
                # t[i] is already claimed by a different s-character
                if t[i] in t_map_s:
                    return False

                # safe to record — register the mapping in both directions
                s_map_t[s[i]] = t[i]     # forward : s-char → t-char
                t_map_s[t[i]] = s[i]     # reverse : t-char → s-char
            else:
            # Type 1 — one-to-many violation:
            # s[i] was seen before but its recorded target differs from t[i]
                if s_map_t[s[i]] != t[i]:
                    return False

        return True     # all positions passed both violation checks


# ── Quick smoke tests ──────────────────────────────────────────
s = Solution()
print(s.isIsomorphic("egg", "add"))             # Expected: True
print(s.isIsomorphic("paper", "title"))         # Expected: True
print(s.isIsomorphic("paperssss", "titlesese")) # Expected: False
print(s.isIsomorphic("f11", "a23"))             # Expected: False

# Note — why two maps instead of one?
#   A single forward map (s → t) catches Type 1 instantly but
#   misses Type 2 entirely. Consider s = "ab", t = "aa":
#     i=0 : s_map_t = {a:a} — no conflict yet
#     i=1 : s_map_t has no entry for 'b', so it records b → a
#           now both 'a' and 'b' map to 'a' — a silent many-to-one
#           that the forward map never detects.
#   The reverse map t_map_s catches this immediately at i=1
#   because 'a' is already in t_map_s from i=0.
#
# Note — two maps visualised for s = "paper", t = "title"
#   i=0  s[i]='p' t[i]='t'  maps: {p:t} | {t:p}  ✓
#   i=1  s[i]='a' t[i]='i'  maps: {p:t,a:i} | {t:p,i:a}  ✓
#   i=2  s[i]='p' t[i]='t'  s_map_t[p]=t == t[i] ✓
#   i=3  s[i]='e' t[i]='l'  maps: {p:t,a:i,e:l} | {t:p,i:a,l:e}  ✓
#   i=4  s[i]='r' t[i]='e'  maps: {p:t,a:i,e:l,r:e} | {t:p,i:a,l:e,e:r}  ✓
#   → True
#
# problem: 205-isomorphic-strings
#
# Time Complexity : O(n)
#   - The loop runs exactly n times                        → O(n)
#   - Every dict lookup and insertion is                  → O(1)
#   - Overall: O(n), a strict improvement over the
#     O(n²) brute-force scan of the previous approach.
#
# Space Complexity: O(k)
#   - s_map_t holds at most k distinct s-characters    → O(k)
#   - t_map_s holds at most k distinct t-characters    → O(k)
#   - For valid ASCII, k ≤ 128                            → O(1)
#   - Overall: O(k), effectively O(1) for fixed alphabets.
# ─────────────────────────────────────────────────────────────