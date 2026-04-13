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
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        # store the length of the given two strings
        s_len = len(s)
        p_len = len(p)

        #  check whether the length of the given string
        #  greater than p or not
        if s_len < p_len:
            return []

        #  construct the character frequency map for the string p
        p_count = Counter(p)
        # initialize the character frequency map for the string s
        s_count = Counter()

        # a list to store p's anagrams starting indices
        anagrams_start_indices = []

        #  iterate the given string s
        for i in range(s_len):
            # update the character frequencies for each character
            s_count[s[i]] = s_count.get(s[i], 0) + 1

            # check the value of i each time
            #  for every value of i
            #  greater than or equal to p_len
            if i >= p_len:
                #  at any given point of time,
                #  in the s_count s's character frequency 
                #  can contain only the number of characters of p's having
                #  with the exact frequency
                # delete the character that doesn't matter or unnecessary
                if s_count[s[i - p_len]] == 1:
                    del s_count[s[i - p_len]]
                #  decrement the unnecessary frequency
                else:
                    s_count[s[i - p_len]] -= 1

            #  check their frequency map are equal or not
            if p_count == s_count:
                # if it is great,
                # insert the starting index
                anagrams_start_indices.append(i - p_len + 1)

        return anagrams_start_indices


s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))

#  time complexity: O(n) n -> length of s
#  space complexity: O(k) k -> number of characters in p