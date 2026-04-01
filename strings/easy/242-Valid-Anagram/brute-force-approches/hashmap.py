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
        
        freq_map = {}

        #  iterate the array
        for i in range(s_len):
            #  get the characters last occurred index stored in the freq_map {}
            j = freq_map.get(t[i], 0)
            
            #  check every time whether j < len(s)
            while j < s_len:
                #  if their values at respective indices matches
                if t[i] == s[j]:
                    #  store the last occurred index in the freq_map {}
                    freq_map[t[i]] = j + 1
                    break
                
                j += 1

            #  if j value equals to len(s)
            #  it has come the end but still did not found the value that matches the character
            if j == s_len:
                return False
        
        return True
    

s = Solution()
print(s.isAnagram("anagram", "nagaram"))
# print(s.isAnagram("rat", "car"))
# print(s.isAnagram("siva", "nisi"))