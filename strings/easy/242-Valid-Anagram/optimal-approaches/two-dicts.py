"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? 
How would you adapt your solution to such a case?
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # variables that store the length of the given two strings
        s_len = len(s)
        t_len = len(t)

        # Check if their lengths matches or not
        if s_len != t_len:
            return False
        
        #  initialize two hashmaps
        s_map = {}
        t_map = {}

        #  iterate the array
        for i in range(t_len):
            #  update the frequencies of each character in the hashmap
            s_map[s[i]] = s_map.get(s[i], 0) + 1
            t_map[t[i]] = t_map.get(t[i], 0) + 1
        
        #  check whether those hashmaps have characters with the same frequency 
        return s_map == t_map
    

s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))
# print(s.isAnagram("siva", "nisi"))