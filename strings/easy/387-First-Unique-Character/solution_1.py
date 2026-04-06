"""
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # store the length of the given string
        s_len = len(s)

        # store the character frequencies of s
        s_char_freq_map = {}

        #  iterate the string s
        for ch in s:
            #  store it's character frequencies in s_char_freq_map
            s_char_freq_map[ch] = s_char_freq_map.get(ch, 0) + 1

        # iterate the string s
        for idx, val in enumerate(s):
            #  check if the character frequency is 'one' or not
            if s_char_freq_map[val] == 1:
                # if it is return the idx
                return idx

        #  If no character is unique return -1
        return -1
        
    
    
s = Solution()
print(s.firstUniqChar("loveleetcode"))
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("aabb"))


# Time Complexity: O(n)
# Space Complexity: O(1)