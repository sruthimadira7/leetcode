"""
796. Rotate String

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.

Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:
Input: s = "abcde", goal = "abced"
Output: false

Constraints:
1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.
"""
# ─────────────────────────────────────────────────────────────
# APPROACH: Doubled String + KMP (Knuth-Morris-Pratt)
#
# Core idea:
#   Every possible rotation of s appears as a substring inside
#   s + s. For example, "abcde" doubled is "abcdeabcde", which
#   contains every rotation — "bcdea", "cdeab", "deabc" and so on.
#   Instead of using Python's `in` (O(n) average but not guaranteed),
#   we use KMP to search for goal inside doubled_s in O(n) worst case.
#
# Algorithm:
#   1. Early exit — if lengths differ, no rotation can match.
#   2. Double s to produce a string that contains every possible
#      rotation of s as a substring.
#   3. Build an LPS array from goal — for each position, record
#      the longest proper prefix that is also a suffix.
#      This lets KMP skip redundant comparisons on a mismatch.
#   4. Use the LPS array to search for goal inside doubled_s.
#      If a full match is found at any position, return True.
#   5. If the search completes without a match, return False.
#
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        # different lengths mean s can never rotate into goal
        if len(s) != len(goal):
            return False

        # doubling s produces a string that contains every possible rotation
        doubled_string = s + s

        # search for goal inside doubled_string using KMP
        return self.kmp_search(doubled_string, goal)

    def kmp_search(self, text: str, pattern: str) -> bool:

        # precompute the LPS array for the pattern to enable smart backtracking
        lps = self.compute_lps(pattern)

        text_index = pattern_index = 0
        text_length = len(text)
        pattern_length = len(pattern)

        # scan through the text one character at a time
        while text_index < text_length:

            if text[text_index] == pattern[pattern_index]:
                # characters match — advance both pointers
                text_index += 1
                pattern_index += 1

                # all characters of pattern matched — found it
                if pattern_index == pattern_length:
                    return True

            elif pattern_index > 0:
                # mismatch after some matches — use LPS to skip redundant comparisons
                pattern_index = lps[pattern_index - 1]

            else:
                # mismatch at the very start — move to the next character in text
                text_index += 1

        # exhausted the text without finding a full match
        return False

    def compute_lps(self, pattern: str) -> list:

        pattern_length = len(pattern)

        # lps[i] = length of the longest proper prefix of pattern[0..i]
        # that is also a suffix — initialised to zero
        lps = [0] * pattern_length

        length = 0   # length of the current matching prefix-suffix
        index = 1    # start from index 1 — lps[0] is always 0

        # build the LPS array character by character
        while index < pattern_length:

            if pattern[index] == pattern[length]:
                # prefix and suffix extended by one — record and advance
                length += 1
                lps[index] = length
                index += 1

            elif length > 0:
                # mismatch — fall back to the previous LPS value and retry
                length = lps[length - 1]

            else:
                # no prefix-suffix match at this position — store zero and move on
                lps[index] = 0
                index += 1

        return lps


# ── Quick smoke tests ──────────────────────────────────────────
s = Solution()
print(s.rotateString("abcde", "cdeab"))   # Expected: True
print(s.rotateString("abcde", "abced"))   # Expected: False

# ─────────────────────────────────────────────────────────────
# Time Complexity : O(n)
#   - compute_lps iterates over goal once                    → O(n)
#   - kmp_search iterates over doubled_string once           → O(2n)
#   - Each character is processed at most twice due to the
#     LPS fallback — no character is compared more than once.
#   - Overall: O(n) worst case.
#
# Space Complexity: O(n)
#   - doubled_string is a new string of length 2n            → O(n)
#   - lps array holds one integer per character in goal      → O(n)
#   - Overall: O(n).
# ─────────────────────────────────────────────────────────────