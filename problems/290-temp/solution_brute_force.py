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
        print(pattern, s)

        s_words = s.split()

        if len(pattern) != len(s_words):
            return False

        s_map = {}
        p_len = len(pattern)

        for i in range(p_len):
            for key, val in s_map.items():
                if key == s_words[i] and val != pattern[i] or key != s_words[i] and val == pattern[i]:
                    return False
            
            s_map[s_words[i]] = pattern[i]


        return True
    

s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))
print(s.wordPattern("aaaa", "dog cat cat dog"))