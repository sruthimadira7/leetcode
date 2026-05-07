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
# APPROACH: Frequency Counter + Bucket Iteration (Counting Sort style)
#
# Core idea:
#   Instead of sorting the frequency map directly, we find the
#   maximum frequency and count down from it. On each level we
#   scan the map and collect every character whose count matches
#   the current level, naturally producing a highest-first order.
#
# Algorithm:
#   1. Iterate over s and build a frequency map s_char_freq
#      that maps each character to its occurrence count.
#   2. Find max_freq — the highest frequency among all characters.
#   3. While max_freq > 0, scan every key in s_char_freq:
#        - If a character's count equals max_freq, append it
#          max_freq times to res.
#   4. Decrement max_freq by 1 and repeat step 3.
#   5. Return res.
#
class Solution:
    def frequencySort(self, s: str) -> str:

        s_char_freq = {}     # frequency map: char → count
        res = ''             # accumulates the final sorted string

        for ch in s:
            # .get(ch, 0) returns 0 on first encounter,
            # then increments on every subsequent visit
            s_char_freq[ch] = s_char_freq.get(ch, 0) + 1   # update frequency

        # highest frequency present in the string
        max_freq = max(s_char_freq.values())

        # count down from max_freq to 1, processing one frequency level per pass
        while max_freq > 0:

            for key in s_char_freq.keys():
                # only collect characters that belong to the current frequency level
                if s_char_freq[key] == max_freq:
                    res += key * max_freq     # repeat character max_freq times and append

            max_freq -= 1     # move down to the next frequency level

        return res


# ── Quick smoke tests ──────────────────────────────────────────
s = Solution()
print(s.frequencySort("tree"))     # Expected: "eert"   (or "eetr")
print(s.frequencySort("cccaaa"))   # Expected: "aaaccc" (or "cccaaa")
print(s.frequencySort("Aabb"))     # Expected: "bbAa"   (or "bbaA")

# Note — why count down instead of sorting?
#   Sorting costs O(k log k). Counting down avoids an explicit
#   sort entirely — the while loop itself imposes the descending
#   frequency order. The trade-off is more iterations overall,
#   giving O(n * k) instead of O(n + k log k).
#
# problem: 451-sort-characters-by-frequency
#
# Time Complexity : O(n * k)
#   - Building s_char_freq iterates over s once          → O(n)
#   - The while loop runs max_freq times        → O(max_freq)
#   - Each iteration scans all k distinct keys           → O(k)
#   - max_freq ≤ n, so the while + for together          → O(n * k)
#   - For a fixed alphabet (a–z, A–Z, 0–9), k ≤ 62,
#     so this approaches O(n) in practice, but in the
#     worst case (all unique chars) it is O(n²).
#
# Space Complexity: O(n + k)
#   - s_char_freq holds at most k distinct entries       → O(k)
#   - res holds all n characters of the output           → O(n)
#   - For a fixed alphabet k is constant, so space
#     is effectively O(n), dominated by the output.
# ─────────────────────────────────────────────────────────────