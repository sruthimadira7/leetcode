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
        
        # Keep tracks of each character last occurred index
        s_is_vistied = [0] * 26 


        # use two nested loops
        for i in range(t_len):
            char = ord(t[i]) - ord('a')
            j = s_is_vistied[char]
            while j < s_len:
                #  check if the two characters at respective indices equal or not
                if t[i] == s[j]:
                    #  stores the last  + 1 occurrence of the given value
                    s_is_vistied[char] = j + 1
                    break
                
                j += 1

            if j == s_len:
                return False
        
        #  check the cnt with length of the t string
        return True
    

s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))
print(s.isAnagram("siva", "nisi"))