"""
49. Group Anagrams
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
# ─────────────────────────────────────────────────────────────
# APPROACH: Brute-Force (Pairwise Frequency Map Comparison)
#
# Core idea:
#   Two strings are anagrams if and only if their character
#   frequency maps are identical. For every word we build its
#   frequency map, then compare it against every word that
#   hasn't been claimed by a group yet, collecting all matches
#   into one group. A visited set prevents a word from being
#   placed into more than one group.
#
# Algorithm:
#   1. Maintain a visited set to track words already assigned
#      to a group.
#   2. For each word at index i (skip if already visited):
#        a. Build its frequency map curr_word_char_freq.
#        b. Start a group curr_word_anagrams = [curr_word].
#        c. Mark curr_word as visited.
#        d. Compare against every later word at index j > i:
#             - Skip if already visited.
#             - Build word's frequency map.
#             - If maps are equal, append to group and mark visited.
#   3. Append the completed group to anagrams_list.
#   4. Return anagrams_list.
#
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        strs_len = len(strs)          # total number of words to process
        anagrams_list = []            # stores all completed anagram groups
        visited = set()               # tracks words already assigned to a group

        for i, curr_word in enumerate(strs):

            if i in visited:          # skip — this word already belongs to a group
                continue

            # build the frequency map for the current word
            curr_word_char_freq = {}
            for ch in curr_word:
                # .get(ch, 0) returns 0 on first encounter,
                # then increments on every subsequent visit
                curr_word_char_freq[ch] = curr_word_char_freq.get(ch, 0) + 1

            curr_word_anagrams = [curr_word]     # every word is an anagram of itself
            visited.add(i)                        # mark curr_word as claimed

            # compare curr_word against every remaining word to the right
            for j in range(i + 1, strs_len):

                if j in visited:      # skip — already placed in an earlier group
                    continue

                word = strs[j]

                # build the frequency map for the candidate word
                word_char_freq = {}
                for ch in word:
                    word_char_freq[ch] = word_char_freq.get(ch, 0) + 1

                # quick pre-check: different number of distinct chars → not anagrams
                if len(curr_word_char_freq) == len(word_char_freq):

                    are_anagrams = True
                    for key in curr_word_char_freq.keys():
                        # any frequency mismatch disqualifies the pair
                        if curr_word_char_freq[key] != word_char_freq.get(key, 0):
                            are_anagrams = False
                            break

                    if are_anagrams:
                        curr_word_anagrams.append(word)   # add to current group
                        visited.add(j)                    # mark word as claimed

            anagrams_list.append(curr_word_anagrams)      # group is complete

        return anagrams_list


# ── Quick smoke tests ──────────────────────────────────────────
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# Expected: [["eat","tea","ate"], ["tan","nat"], ["bat"]] (any order)
print(s.groupAnagrams([""]))       # Expected: [[""]]
print(s.groupAnagrams(["a"]))      # Expected: [["a"]]

# problem: 49-group-anagrams
#
# Time Complexity : O(n² * m)
#   - Outer loop runs n times                              → O(n)
#   - Inner loop runs up to n times per outer iteration   → O(n)
#   - Building each frequency map iterates over the word  → O(m)
#   - Overall: O(n² * m), where m is the average word length.
#
# Space Complexity: O(n * m)
#   - visited set holds at most n indices                 → O(n)
#   - anagrams_list holds all n words across all groups   → O(n * m)
#   - Two frequency maps held at a time, each size ≤ 26   → O(1)
#   - Overall: O(n * m), dominated by the output list.
# ─────────────────────────────────────────────────────────────