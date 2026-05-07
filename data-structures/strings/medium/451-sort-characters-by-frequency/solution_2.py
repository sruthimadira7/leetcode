"""
Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

Constraints:
1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.
"""
# ─────────────────────────────────────────────────────────────
# APPROACH: Hash Map (Frequency Counter)
#
# Core idea:
#   Characters that appear more times should come first in the
#   result. We build a frequency map for s, sort the entries
#   by count in descending order, then reconstruct the string
#   by repeating each character exactly as many times as it occurs.
#
# Algorithm:
#   1. Iterate over s and build a frequency map s_counter
#      that maps each character to its occurrence count.
#   2. Sort the (character, count) pairs by count, highest first.
#   3. For each (character, count) pair, append the character
#      repeated count times to the result string res.
#   4. Return res.
#
class Solution:
    def frequencySort(self, s: str) -> str:

        s_counter = {}     # frequency map: char → count
        res = ''             # accumulates the final sorted string

        for ch in s:
            # .get(ch, 0) returns 0 on first encounter,
            # then increments on every subsequent visit
            s_counter[ch] = s_counter.get(ch, 0) + 1   # update frequency

        # sort (char, count) pairs by count descending
        sorted_s = sorted(s_counter.items(), key=lambda item: item[1], reverse=True)

        for (ch, cnt) in sorted_s:
            res += ch * cnt     # repeat each character cnt times and append

        return res


# ── Quick smoke tests ──────────────────────────────────────────
s = Solution()
print(s.frequencySort("tree"))     # Expected: "eert"   (or "eetr")
print(s.frequencySort("cccaaa"))   # Expected: "aaaccc" (or "cccaaa")
print(s.frequencySort("Aabb"))     # Expected: "bbAa"   (or "bbaA")

# Note — case sensitivity:
#   'A' and 'a' are treated as distinct characters because
#   Python dict keys are case-sensitive. No special handling needed.
#
# problem: 451-sort-characters-by-frequency
#
# Time Complexity : O(n + k log k)
#   - Building s_counter iterates over s once      → O(n)
#   - sorted() sorts at most k distinct characters   → O(k log k)
#   - Rebuilding res repeats chars totalling n        → O(n)
#   - Overall: O(n + k log k); for fixed alphabets
#     (a–z, A–Z, 0–9), k ≤ 62, so this approaches O(n).
#
# Space Complexity: O(n + k)
#   - s_counter holds at most k distinct entries   → O(k)
#   - res holds all n characters of the output       → O(n)
#   - For a fixed alphabet k is constant, so space
#     is effectively O(n), dominated by the output.
# ─────────────────────────────────────────────────────────────