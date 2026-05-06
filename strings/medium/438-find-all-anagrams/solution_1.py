"""
438. Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""
# ─────────────────────────────────────────────────────────────
# APPROACH: Sliding Window (Fixed-Size) + Frequency Map
#
# Core idea:
#   A window of exactly p_len characters slides across s one
#   step at a time. At every position we maintain a live
#   frequency map s_count for the current window. If s_count
#   matches p_count at any position, the window is an anagram
#   of p and its start index is recorded.
#   Adding one character on the right and removing one on the
#   left keeps each update O(1), making the overall scan O(n).
#
# Algorithm:
#   1. Early-exit if s is shorter than p — no window can fit.
#   2. Build p_count once using Counter(p).
#   3. Slide index i from 0 to s_len - 1:
#        a. Add s[i] to s_count (expand right edge of window).
#        b. Once i >= p_len, the window has exceeded p_len chars —
#           remove the character that just fell off the left edge
#           s[i - p_len]. Delete its key entirely if its count
#           drops to zero, keeping s_count lean for comparison.
#        c. Compare s_count == p_count. If equal, the window
#           starting at (i - p_len + 1) is an anagram — record it.
#   4. Return anagrams_start_indices.
#
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        s_len = len(s)
        p_len = len(p)

        if s_len < p_len:          # no window of size p_len can fit inside s
            return []

        p_count = Counter(p)       # fixed reference frequency map for p
        s_count = Counter()        # live frequency map for the current window

        anagrams_start_indices = []     # collects valid window start positions

        for i in range(s_len):

            # ── expand the right edge ──────────────────────────
            # bring s[i] into the current window
            s_count[s[i]] = s_count.get(s[i], 0) + 1    # add incoming character

            # ── shrink the left edge (once window exceeds p_len) ──
            if i >= p_len:
                # s[i - p_len] is the character that just fell off the left
                if s_count[s[i - p_len]] == 1:
                    del s_count[s[i - p_len]]    # remove key entirely to keep maps comparable
                else:
                    s_count[s[i - p_len]] -= 1   # decrement — character still present in window

            # ── check for anagram match ────────────────────────
            # window is exactly p_len wide when i >= p_len - 1
            if p_count == s_count:
                anagrams_start_indices.append(i - p_len + 1)   # record start index of this window

        return anagrams_start_indices


# ── Quick smoke tests ──────────────────────────────────────────
s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))   # Expected: [0, 6]
print(s.findAnagrams("abab", "ab"))          # Expected: [0, 1, 2]
print(s.findAnagrams("aa", "bb"))            # Expected: []

# Note — why delete the key instead of setting it to 0?
#   Counter and dict equality checks compare both keys and values.
#   If s_count retains a key with value 0 that p_count doesn't have,
#   the two maps will never compare equal even if all frequencies match.
#   Deleting the key keeps s_count structurally identical to p_count
#   whenever the window is a valid anagram.
#
# Note — sliding window visualised for s = "cbaebabacd", p = "abc"
#   i=0  window="c"     s_count={c:1}           p_count={a:1,b:1,c:1}  ✗
#   i=1  window="cb"    s_count={c:1,b:1}       p_count={a:1,b:1,c:1}  ✗
#   i=2  window="cba"   s_count={c:1,b:1,a:1}   p_count={a:1,b:1,c:1}  ✓ → index 0
#   i=3  window="bae"   s_count={b:1,a:1,e:1}   p_count={a:1,b:1,c:1}  ✗
#   ...
#   i=8  window="bac"   s_count={b:1,a:1,c:1}   p_count={a:1,b:1,c:1}  ✓ → index 6
#
# problem: 438-find-all-anagrams-in-a-string
#
# Time Complexity : O(n)
#   - Building p_count scans p once                       → O(p_len)
#   - The for loop scans s once                           → O(s_len)
#   - Each add / delete / decrement is a O(1) dict op     → O(1)
#   - Map comparison holds at most 26 keys (lowercase)    → O(1)
#   - Overall: O(n), where n = s_len.
#
# Space Complexity: O(k)
#   - p_count holds at most k distinct characters of p    → O(k)
#   - s_count holds at most k distinct characters         → O(k)
#   - For lowercase English letters, k ≤ 26              → O(1)
#   - Overall: O(k), effectively O(1) for fixed alphabets.
# ─────────────────────────────────────────────────────────────