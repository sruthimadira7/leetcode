"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""
#────────────────────────────────────────────────────────────────────────────────
# APPROACH: Reverse Two-Phase Scan (Skip-then-Count, Single Pointer)
#────────────────────────────────────────────────────────────────────────────────
#
# Core idea:
#   The last word is whatever non-space run sits at the right end of the string,
#   ignoring any trailing spaces after it. So we scan from the RIGHT in two phases:
#   first slide past any trailing spaces, then count letters until we hit a space
#   or run out of string. Scanning from the end means we never have to look at the
#   earlier words at all — we touch only the trailing spaces plus the last word.
#   This exploits the fact that the answer depends solely on the tail of s.
#
# Algorithm:
#   1. Set pointer i to the last index, len(s) - 1.
#   2. PHASE 1 (skip spaces): while i >= 0 and s[i] == " ", decrement i.
#      Now i points at the final character of the last word (or i < 0 if the
#      string were all spaces — excluded here by the constraints).
#   3. Initialize len_last_word = 0.
#   4. PHASE 2 (count letters): while i >= 0 and s[i] != " ", increment the
#      counter and decrement i. Stop at the first space to the word's left, or
#      when i falls below 0 (the word starts the string).
#   5. Return len_last_word.
#
# Visualization:
#   Example: "   fly me   to   the moon  "
#   index:    0 1 2 3 4 5 6 7 ...                    24 25 26
#   chars:    ' '' '' ' f  l  y ' ' m  e ... m  o  o  n  ' '' '
#                                                          ^ i starts at last index 26
#
#   PHASE 1 — skip trailing spaces:
#     i=26 ' ' → skip      i=25 ' ' → skip      i=24 'n' → stop
#     ...   the   m  o  o  n  ' '' '
#                          ^ i now rests on 'n'
#
#   PHASE 2 — count the word, walking left:
#     'n' → cnt 1   'o' → cnt 2   'o' → cnt 3   'm' → cnt 4   then s[i]=' ' → stop
#     ...   the   m  o  o  n
#                 └─────────┘ counted 4
#
#   Final: return 4
#
# Why this approach works:
#   Splitting into "skip spaces" then "count non-spaces" cleanly handles the messy
#   trailing-whitespace cases without trimming or allocating a new string, and the
#   right-to-left direction means we measure exactly the last word and nothing else.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # initailize i to the last index of the given string 
        i = len(s) - 1

        # loop until i is greater than or equal to 'zero' & s[i] is equal to white-space characters
        while i >= 0 and s[i] == " ":
            #  decrement i by 'one'
            i -= 1
        
        #  initalize len_last_word to 'zero'
        len_last_word = 0
        # loop until i is greater than or equal to 'zero' and s[i] is not equal to white-space characters
        #  if it encounters a space then it's done traversing the last word
        while i >= 0 and s[i] != " ":
            #  increment len_last_word by 'one'
            len_last_word += 1
            #   decrement i by 'one'
            i -= 1

        return len_last_word



s = Solution()
print(s.lengthOfLastWord("   fly me   to   the moon  "))
print(s.lengthOfLastWord("luffy is still joyboy"))

#────────────────────────────────────────────────────────────────────────────────
# COMPLEXITY ANALYSIS
#────────────────────────────────────────────────────────────────────────────────
#
# Time Complexity: O(t + w), worst case O(n)
#   - t = number of trailing spaces, w = length of the last word.
#   - Phase 1 touches each trailing space once; Phase 2 touches each letter of the
#     last word once. We never look at the rest of the string.
#   - Worst case (e.g. "a" or one long word with no trailing spaces) → O(n), but
#     typically far less than scanning the whole string.
#   - Each step is O(1).
#
# Space Complexity: O(1)
#   - Only an index i and a counter len_last_word.
#   - No new strings, splits, or auxiliary structures.
#
# Why not better?
#   - We must read every character of the last word to know its length, so O(w) is
#     unavoidable. The two-phase scan already touches the minimum needed (the tail),
#     making it optimal for this problem.


#────────────────────────────────────────────────────────────────────────────────
# COMMON PITFALLS & HOW TO AVOID THEM
#────────────────────────────────────────────────────────────────────────────────
#
# 1. Off-by-one at the start
#    Pitfall: Initializing i = len(s) instead of len(s) - 1 → IndexError on s[i].
#    How to avoid: Remember the last valid index is len(s) - 1.
#    Why it matters: s[len(s)] is out of range and crashes immediately.
#
# 2. Forgetting trailing spaces (the whole trap of this problem)
#    Pitfall: Counting from the end without skipping spaces first → on "moon  "
#             you'd start on a space, count 0, and return 0.
#    How to avoid: Phase 1 explicitly slides past trailing spaces before counting.
#    Why it matters: Examples 2's "...moon  " has two trailing spaces; skipping
#             this phase returns 0 instead of 4.
#
# 3. Missing the i >= 0 guard
#    Pitfall: while s[i] != " " without the bound → when the last word starts at
#             index 0 (e.g. "joyboy"), i decrements to -1 and s[-1] wraps to the
#             LAST character, looping wrongly or miscounting.
#    How to avoid: Always pair the index check `i >= 0` BEFORE the char check, so
#             short-circuit evaluation stops before the bad index.
#    Why it matters: Python's negative indexing makes this a silent logic bug, not
#             a crash — the hardest kind to spot.
#
# 4. Equal / repeated characters
#    Pitfall: Assuming letters in the word are distinct.
#    How to avoid: We only compare against the space character, never letters to
#             each other, so repeats like "moon" (double 'o') are handled naturally.
#    Why it matters: A naive "count distinct chars" approach would return 3 for
#             "moon" instead of 4.
#
# 5. Boundary: word at the very start vs. end
#    Pitfall: Special-casing the first word or the last character.
#    How to avoid: The `i >= 0` guard in BOTH loops unifies the logic — a word
#             touching index 0 just exits via the bound instead of via a space.
#    Why it matters: "luffy is still joyboy" has no trailing spaces and the answer
#             word ends the string; the same code path handles it.
#
# 6. Type confusion
#    Pitfall: Comparing s[i] to ' ' assumes s is a string of chars; passing a list
#             of words instead would compare against the wrong unit.
#    How to avoid: Confirm input is a single string (the signature says `s: str`).
#    Why it matters: Feeding ["fly","moon"] would treat "moon" != " " as a whole-
#             element comparison and count words, not letters.
#
# 7. Constraint at scale (up to 10^4 chars)
#    Pitfall: Using s.split() then [-1] — correct, but builds a full list of every
#             word, O(n) extra space, even though we only want the last.
#    How to avoid: The two-phase scan stays O(1) space and stops early.
#    Why it matters: On a 10,000-char line of many words, split allocates the entire
#             word list just to read one element.


#────────────────────────────────────────────────────────────────────────────────
# ALTERNATIVE APPROACHES (Why we didn't use them)
#────────────────────────────────────────────────────────────────────────────────
#
# Approach 2: split() and take the last element
#   Code: return len(s.split()[-1])
#   Pros: One line, extremely readable; split() ignores extra/trailing spaces.
#   Cons: Allocates a list of ALL words → O(n) extra space, and processes the whole
#         string even though only the tail matters.
#   Complexity: O(n) time, O(n) space.
#   When to use: Quick scripts where clarity beats micro-optimization.
#
# Approach 3: rstrip() then rfind(" ")
#   Code: s = s.rstrip(); return len(s) - 1 - s.rfind(" ")
#   Pros: Concise; rfind locates the last space directly.
#   Cons: rstrip builds a trimmed COPY (O(n) space), and the index arithmetic is
#         easy to get wrong by one.
#   Complexity: O(n) time, O(n) space.
#   When to use: When string methods are clearer to your team than manual pointers.


#────────────────────────────────────────────────────────────────────────────────
# VARIATIONS & FOLLOW-UP QUESTIONS
#────────────────────────────────────────────────────────────────────────────────
#
# "What if you needed the length of the FIRST word instead?"
#   → Scan forward: skip leading spaces (i from 0 up while s[i]==' '), then count
#     non-spaces until a space or end. Mirror image of this solution.
#
# "What if you needed to return the last word itself, not its length?"
#   → Track the end index (right after Phase 1, end = i) and the start index (i+1
#     after Phase 2), then return s[i+1:end+1].
#
# "What if words could be separated by tabs/newlines too?"
#   → Replace the `== " "` test with `s[i].isspace()` to treat all whitespace as
#     separators.
#
# "Can you solve it with O(1) space?"
#   → Yes — this solution already is. It uses only an index and a counter, no copies
#     or splits.


#────────────────────────────────────────────────────────────────────────────────
# INTERVIEW TIPS
#────────────────────────────────────────────────────────────────────────────────
#
# When asked this in an interview:
# 1. Clarify: "Can there be trailing spaces? Multiple spaces between words? Is the
#    string guaranteed non-empty / to contain a word?" (Here, yes, yes, yes.)
# 2. Walk an example: Use "   fly me   to   the moon  " → 4 and point out the two
#    trailing spaces that must be skipped first.
# 3. State approach before coding: "Scan from the right, skip trailing spaces, then
#    count letters until the next space — O(1) space, no split."
# 4. Mention complexity: O(t + w) time, O(1) space; contrast with split()'s O(n)
#    space to show you know the trade-off.
# 5. Test edge cases aloud: single word "a", word at index 0 with no trailing space,
#    many spaces between words, trailing spaces only after the last word.
# 6. Discuss improvements: generalize to arbitrary whitespace via isspace(), or
#    returning the word/its position instead of just the length.


#────────────────────────────────────────────────────────────────────────────────
# LEARNING VALUE: Why You Should Know This
#────────────────────────────────────────────────────────────────────────────────
#
# This problem teaches:
#   ✓ Two-phase pointer scanning - "skip the noise, then measure the signal" is a
#                                   reusable shape for tokenizing and trimming.
#   ✓ Short-circuit bounds checking - putting `i >= 0` before s[i] prevents the
#                                      negative-index wraparound that bites beginners.
#   ✓ Avoiding unnecessary allocation - solving in place instead of split()/strip()
#                                        builds the instinct for O(1)-space solutions.
#
# These concepts appear in:
#   - Problem A: Reverse Words in a String
#   - Problem B: Valid Palindrome (skip non-alphanumerics with two pointers)
#   - Real-world scenario: Parsing the final token of a command line or trimming
#                          trailing whitespace from user input / log entries.


#────────────────────────────────────────────────────────────────────────────────
# PATTERN CATEGORY: Which DSA Pattern Family Does This Belong To?
#────────────────────────────────────────────────────────────────────────────────
#
# This is a: Single-Pointer Linear Scan (two-phase, right-to-left) — a lightweight
#            cousin of the Two Pointers family.
#
# Pattern Chain:
#   Basic string traversal → THIS PROBLEM (skip-then-count scan)
#                          → Two Pointers (reverse words, palindrome checks)
#                          → Tokenizer / Parser state machines
#
# Why it's foundational:
#   It combines directional scanning with a tiny state change (spaces → letters),
#   which is exactly the seed idea behind tokenizers and two-pointer techniques,
#   while still using only O(1) space and no data structures.
#
# Build on this to learn:
#   - Two Pointers (opposite-end and same-direction variants)
#   - Sliding Window (longest word, longest substring conditions)
#   - String tokenization / simple lexers