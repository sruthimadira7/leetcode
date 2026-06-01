"""
Given a string s, return true if it is a palindrome, or false otherwise.

A string is a palindrome that reads the same backwards as forwards.
Convert all uppercase letters into lowercase letters and remove all non-alphanumeric
characters in this problem.

Alphanumeric characters include letters and numbers.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
"""
#────────────────────────────────────────────────────────────────────────────────
# APPROACH: Two Pointers with In-Place Filtering (Skip + Converge)  ← code above
#────────────────────────────────────────────────────────────────────────────────
#
# Core idea:
#   This is the standard converging two-pointer palindrome check, upgraded to
#   ignore the "noise": spaces, punctuation, and letter case. Instead of building
#   a cleaned-up copy of the string first, we filter ON THE FLY — whenever a
#   pointer lands on a non-alphanumeric character, we slide it past that character
#   before comparing. We compare the survivors case-insensitively with .lower().
#   This exploits the same symmetry as a plain palindrome, but layers a "skip the
#   junk" step on top so we never allocate a second string.
#
# Algorithm:
#   1. Put left at index 0 and right at the last index, len(s) - 1.
#   2. While left < right:
#   3.    Advance left rightward past any non-alphanumeric char (inner while).
#   4.    Retreat right leftward past any non-alphanumeric char (inner while).
#   5.    Compare s[left].lower() with s[right].lower(). Mismatch → return False.
#   6.    Step both pointers inward (left += 1, right -= 1) and repeat.
#   7. If the loop finishes with no mismatch, return True.
#
# Visualization:
#   Example: "A man, a plan, a canal: Panama"
#   (showing the key moves; '.' marks a skipped non-alnum char)
#
#   Start:  A   m a n ,   a   ...   P a n a m a
#           ^                                   ^
#         left                               right
#
#   left on 'A' (alnum, keep) ; right on 'a' (alnum, keep)
#   compare 'a' vs 'a' → match → step inward
#
#   Later, left lands on ' ' or ',' → inner loop skips it:
#           ... n ,   a ...
#               ^skip→^ now on 'a'
#
#   Each comparison is between two filtered, lowercased chars. Pointers meet in the
#   middle with no mismatch → return True.
#
# Why this approach works:
#   Skipping non-alphanumerics makes the pointers behave as if the string were
#   already cleaned, and .lower() neutralizes case — so the mirrored comparison
#   exactly matches the problem's definition, all in O(1) extra space.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointers at the two ends of the string.
        left = 0
        right = len(s) - 1

        # Converge inward until the pointers meet or cross.
        while left < right:
            # Skip anything that isn't a letter or digit on the LEFT side.
            # The `left < right` guard inside stops us from running past the
            # right pointer when the string is all punctuation.
            while left < right and not s[left].isalnum():
                left += 1
            # Same skip on the RIGHT side, moving inward.
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare the two valid characters case-insensitively.
            if s[left].lower() != s[right].lower():
                return False

            # Both matched — step inward and continue.
            left += 1
            right -= 1

        return True


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(s.isPalindrome("race a car"))                      # False
print(s.isPalindrome("0P"))                              # False  ('0' vs 'p')
print(s.isPalindrome(" "))                               # True   (empty after filtering)
print(s.isPalindrome("A   ma"))                          # False  ('a' vs 'a'? -> "ama" -> True)

#────────────────────────────────────────────────────────────────────────────────
# COMPLEXITY ANALYSIS
#────────────────────────────────────────────────────────────────────────────────
#
# Time Complexity: O(n)
#   - Each pointer moves only inward and never backtracks. Across the whole run,
#     left and right together traverse the string at most once → O(n).
#   - The inner skip-loops don't add an extra factor: every index is skipped or
#     compared exactly once total, not re-examined.
#   - .isalnum() and .lower() on a single char are O(1).
#
# Space Complexity: O(1)
#   - Only two integer pointers. No cleaned/reversed copy is built.
#   - (Note: s.lower() on a single character creates a tiny temporary, but it's
#     constant size — not proportional to n.)
#
# Why not better?
#   - We must inspect each alphanumeric character of (at least) the first half to
#     confirm symmetry, so O(n) is the floor. Pre-filtering into a new string would
#     also be O(n) time but cost O(n) space — this in-place version is strictly
#     leaner.


#────────────────────────────────────────────────────────────────────────────────
# COMMON PITFALLS & HOW TO AVOID THEM
#────────────────────────────────────────────────────────────────────────────────
#
# 1. Missing the inner `left < right` guard
#    Pitfall: Writing `while not s[left].isalnum(): left += 1` without the bound.
#             On an all-punctuation string like ".,!" left marches off the end and
#             s[left] throws IndexError.
#    How to avoid: Keep `left < right and ...` in BOTH inner loops so the skip can
#             never overrun the other pointer.
#    Why it matters: Example 3 (" ") and inputs like ".," depend on this — the
#             pointers must be allowed to cross during skipping and exit cleanly.
#
# 2. Off-by-one on the right pointer
#    Pitfall: right = len(s) instead of len(s) - 1 → out-of-range on first access.
#    How to avoid: Last valid index is len(s) - 1.
#    Why it matters: s[len(s)] raises IndexError immediately.
#
# 3. Empty-after-filtering input
#    Pitfall: Treating " " or "!!!" as non-palindromes.
#    How to avoid: After skipping, left and right cross, the outer loop ends, and we
#             return True — the correct answer for an empty filtered string.
#    Why it matters: Example 3 expects True for " "; the skip-then-cross flow gives
#             it for free.
#
# 4. Forgetting case-insensitivity
#    Pitfall: Comparing s[left] to s[right] without .lower() → 'A' != 'a' fails a
#             valid palindrome.
#    How to avoid: Lowercase BOTH sides before comparing.
#    Why it matters: Example 1 starts with 'A' (capital) vs ending 'a' (lowercase);
#             without .lower() it wrongly returns False.
#
# 5. Digits-vs-letters confusion (the "0P" trap)
#    Pitfall: Assuming alphanumeric means "letters only" and skipping digits, or
#             assuming a digit can't break a palindrome.
#    How to avoid: .isalnum() treats digits AND letters as valid; '0' and 'p' are
#             both kept and compared.
#    Why it matters: "0P" filters to "0p"; '0' != 'p' → False. A letters-only filter
#             would wrongly drop the '0' and return True.
#
# 6. Type confusion
#    Pitfall: .isalnum() behaves differently on bytes vs str; on non-ASCII it also
#             accepts Unicode letters/digits.
#    How to avoid: Confirm s is a str of the expected charset; constraints here say
#             printable ASCII, so .isalnum() is safe.
#    Why it matters: On bytes objects the methods don't exist the same way, causing
#             attribute errors.
#
# 7. Constraint at scale (n up to 2 * 10^5)
#    Pitfall: Pre-cleaning via `''.join(c.lower() for c in s if c.isalnum())` then
#             checking == reversed — correct but O(n) extra space.
#    How to avoid: The in-place two-pointer scan stays O(1) space and handles the
#             max input comfortably.
#    Why it matters: At 200k characters the cleaned copy needlessly doubles memory.


#────────────────────────────────────────────────────────────────────────────────
# ALTERNATIVE APPROACHES (Why we didn't use them)
#────────────────────────────────────────────────────────────────────────────────
#
# Approach 2: Filter then compare with reverse
#   Code: t = [c.lower() for c in s if c.isalnum()]; return t == t[::-1]
#   Pros: Very readable; the palindrome check itself is trivial after cleaning.
#   Cons: Builds a filtered list AND its reversal → O(n) extra space, violating the
#         spirit of the O(1) follow-up. Always processes the whole string.
#   Complexity: O(n) time, O(n) space.
#   When to use: Quick scripts where clarity matters more than memory.
#
# Approach 3: Filter then two pointers on the cleaned string
#   Idea: First produce the cleaned string, then run the plain opposite-end pointer
#         check on it.
#   Pros: Separates "cleaning" from "checking", easy to reason about.
#   Cons: Still O(n) space for the cleaned copy; two passes instead of one.
#   Complexity: O(n) time, O(n) space.
#   When to use: When the cleaned string is needed elsewhere too, so the copy isn't
#         wasted.


#────────────────────────────────────────────────────────────────────────────────
# VARIATIONS & FOLLOW-UP QUESTIONS
#────────────────────────────────────────────────────────────────────────────────
#
# "Can you do it in O(1) extra space?"
#   → Yes — the in-place skip-and-converge version above already is; nothing is
#     copied.
#
# "What if you may delete at most ONE character to make it a palindrome?"
#   → On the first mismatch, try skipping either the left or the right char and
#     verify the remaining range is a palindrome. O(n) time. (LeetCode #680.)
#
# "What if you should ignore case but KEEP punctuation as significant?"
#   → Drop the .isalnum() skip-loops and keep only the .lower() comparison.
#
# "What if non-ASCII / Unicode letters are allowed?"
#   → .isalnum() and .lower() already accept Unicode in Python, but consider
#     Unicode normalization (NFC/NFD) for accented characters and casefold() instead
#     of lower() for robust case handling.
#
# "What if the input were a stream you can't index randomly?"
#   → You'd need a different strategy (e.g. buffer + reverse, or a deque), since
#     two-end pointers require random/back access.


#────────────────────────────────────────────────────────────────────────────────
# INTERVIEW TIPS
#────────────────────────────────────────────────────────────────────────────────
#
# When asked this in an interview:
# 1. Clarify: "Ignore case AND non-alphanumerics? Are digits significant? Is the
#    empty/blank string a palindrome?" (Here: yes, yes — digits count, and blank → True.)
# 2. Walk an example: "A man, a plan, a canal: Panama" → filtered
#    "amanaplanacanalpanama" reads the same both ways → True.
# 3. State approach before coding: "Two pointers from both ends; skip non-alnum
#    chars on each side, compare lowercased — O(n) time, O(1) space, no cleaned copy."
# 4. Mention complexity: O(n)/O(1), and contrast with the filter-then-reverse
#    one-liner's O(n) space.
# 5. Test edge cases aloud: " " (blank → True), "0P" (digit vs letter → False),
#    all-punctuation ".,!" (→ True), single char.
# 6. Discuss improvements: extend to "delete at most one char" (#680); mention
#    casefold() and Unicode normalization for international text.


#────────────────────────────────────────────────────────────────────────────────
# LEARNING VALUE: Why You Should Know This
#────────────────────────────────────────────────────────────────────────────────
#
# This problem teaches:
#   ✓ Two pointers + in-place filtering - skipping unwanted elements WHILE scanning,
#                                         instead of pre-cleaning, to save space.
#   ✓ Guarded inner loops - the `left < right` inside each skip-loop is the subtle
#                           detail that prevents overruns on all-junk inputs.
#   ✓ Normalization before comparison - lowercasing (and the idea of casefold /
#                                       Unicode normalization) for fair equality.