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
        
        #  create two arrays 
        s_arr = [0] * 26
        t_arr = [0] * 26

        #  first-loop
        for i in range(t_len):
            # update frequencies of each character 
            s_arr[ord(s[i]) - ord('a')] += 1
            t_arr[ord(t[i]) - ord('a')] += 1
        
        # check whether they have the characters with same frequency
        return s_arr == t_arr
    

s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))
print(s.isAnagram("siva", "nisi"))