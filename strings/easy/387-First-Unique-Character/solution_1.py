"""
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.
"""
# ─────────────────────────────────────────────────────────────
# APPROACH: Two-Pass Frequency Map
#
# Core idea:
#   A character is unique if it appears exactly once in s.
#   We first build a complete frequency map in one pass, then
#   make a second pass in original order to find the first
#   character whose count is exactly 1. The two-pass structure
#   guarantees we respect the original index order while still
#   having global frequency knowledge.
#
# Algorithm:
#   1. Iterate over s and build s_counter, mapping each
#      character to its total occurrence count.
#   2. Iterate over s a second time using enumerate:
#        - If s_counter[val] == 1, this is the first
#          non-repeating character — return its index idx.
#   3. If no unique character is found, return -1.
#
class Solution:
    def firstUniqChar(self, s: str) -> int:

        s_len = len(s)
        s_counter = {}     # frequency map: char → total occurrence count

        # ── Pass 1 : build the complete frequency map ──────────
        for ch in s:
            # .get(ch, 0) returns 0 on first encounter,
            # then increments on every subsequent visit
            s_counter[ch] = s_counter.get(ch, 0) + 1   # update frequency

        # ── Pass 2 : find the first character with frequency 1 ─
        for idx, val in enumerate(s):
            # frequency of 1 means this character never repeated
            if s_counter[val] == 1:
                return idx     # return immediately — leftmost unique character found

        return -1     # no unique character exists in s


# ── Quick smoke tests ──────────────────────────────────────────
s = Solution()
print(s.firstUniqChar("loveleetcode"))   # Expected: 2  ('v')
print(s.firstUniqChar("leetcode"))       # Expected: 0  ('l')
print(s.firstUniqChar("aabb"))           # Expected: -1

# Note — why two passes instead of one?
#   A single pass cannot determine uniqueness on the fly because
#   a character that appears unique at index i might repeat at
#   index j > i. The full frequency map must be complete before
#   any uniqueness judgement can be made. Two passes are the
#   minimum required for correctness.
#
# Note — two-pass visualised for s = "loveleetcode"
#   Pass 1 frequency map:
#     {l:1, o:2, v:1, e:4, t:1, c:1, d:1}
#
#   Pass 2 scan:
#     idx=0  'l'  freq=1  ✗  (wait — l appears once? yes → return 0?)
#     idx=0  'l'  freq=1  → but expected output is 2, let's re-check:
#     s = "loveleetcode"
#     {l:1, o:2, v:1, e:4, t:1, c:1, d:1}
#     idx=0  'l'  freq=1  ✓  → return 0?
#     No — expected is 2 because 'l' does appear once but 'o' repeats,
#     wait: l=1 so idx 0 should return 0... but expected says 2.
#     Re-counting: l-o-v-e-l-e-e-t-c-o-d-e → l:2, o:2, v:1, e:4 ...
#     idx=0  'l'  freq=2  ✗
#     idx=1  'o'  freq=2  ✗
#     idx=2  'v'  freq=1  ✓  → return 2
#
# Time Complexity : O(n)
#   - Pass 1 iterates over s once to build the map      → O(n)
#   - Pass 2 iterates over s once to find the answer    → O(n)
#   - Every dict lookup and insertion is                → O(1)
#   - Overall: O(n).
#
# Space Complexity: O(k)
#   - s_counter holds at most k distinct chars    → O(k)
#   - s consists of lowercase English letters, k ≤ 26  → O(1)
#   - Overall: O(k), effectively O(1) for fixed alphabets.
# ─────────────────────────────────────────────────────────────