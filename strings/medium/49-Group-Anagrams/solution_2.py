"""
49. Group Anagrams
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form each other.
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
# APPROACH: Hash Map (Sorted Word as Key)
#
# Core idea:
#   Two strings are anagrams if and only if their sorted
#   characters are identical. So sorting each word produces
#   a canonical key that is shared by all words in the same
#   anagram group. We use a defaultdict(list) to automatically
#   bucket every word under its canonical key.
#
# Algorithm:
#   1. Create a defaultdict(list) called anagrams to map each
#      canonical key to the list of words that share it.
#   2. For each word in strs:
#        a. Sort the word's characters to produce a canonical key.
#        b. Append the original word under that key.
#   3. Collect all bucket lists from anagrams.values() into
#      anagrams_list and return it.
#
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        anagrams = defaultdict(list)     # canonical key → [words that share it]
        anagrams_list = []               # stores all completed anagram groups

        for word in strs:
            # sorting the word produces the same key for all its anagrams
            # e.g. "eat" → "aet",  "tea" → "aet",  "ate" → "aet"
            key = ''.join(sorted(word))       # canonical key for this anagram group
            anagrams[key].append(word)        # place word into the correct bucket

        # each value in the defaultdict is one complete anagram group
        for items in anagrams.values():
            anagrams_list.append(items)       # collect each group into the result

        return anagrams_list


# ── Quick smoke tests ──────────────────────────────────────────
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# Expected: [["eat","tea","ate"], ["tan","nat"], ["bat"]] (any order)
print(s.groupAnagrams([""]))       # Expected: [[""]]
print(s.groupAnagrams(["a"]))      # Expected: [["a"]]

# Note — why defaultdict(list)?
#   A regular dict would raise a KeyError on the first append
#   for any new key. defaultdict(list) automatically initialises
#   a new empty list for every unseen key, removing the need for
#   an explicit `if key not in anagrams` guard.
#
# Note — can the collection step be simplified?
#   Yes. The for loop that builds anagrams_list is equivalent to:
#       return list(anagrams.values())
#   Both are correct; the explicit loop mirrors your personal style.
#
# problem: 49-group-anagrams
#
# Time Complexity : O(n * m log m)
#   - The outer loop runs once per word                   → O(n)
#   - sorted(word) sorts each word of length m            → O(m log m)
#   - ''.join() and dict lookup are both                  → O(m)
#   - Overall: O(n * m log m), where m is the average word length.
#
# Space