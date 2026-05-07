"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. 

Specifically:
Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Explanation:
The bijection can be established as:
'a' maps to "dog".
'b' maps to "cat".

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_words = s.split()
        print(s_words)

        if len(pattern) != len(s_words):
            return False

        p_map_s = {}
        s_map_p = {}
        n = len(pattern)

        for i in range(n):
            if pattern[i] not in p_map_s:
                if s_words[i] in s_map_p:
                    return False
                
                p_map_s[pattern[i]] = s_words[i]
                s_map_p[s_words[i]] = pattern[i]

            else:
                if p_map_s[pattern[i]] != s_words[i]:
                    return False

        return True

s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))
print(s.wordPattern("abba", "dog cat cat fish"))