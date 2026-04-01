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
        
        #  initialzie a hashmap
        freq_map = {}

        #  iterate the t string
        for i in range(t_len):
            #  store all its characters and their frequencies together in a hashmap
            freq_map[t[i]] = freq_map.get(t[i], 0) + 1

        #  iterate the other string
        for j in range(s_len):
            #  check whether the character at the current index is present in the hashmap or not
            #  also check whether the vale of the character is 'zero'
            #  they are not anagrams
            if s[j] not in freq_map or freq_map[s[j]] == 0:
                return False
            
            # If the character is present and it's frequency is greater than 0 
            # Update it's frequency value by decrementing with 1 
            freq_map[s[j]] -= 1

        return True
    

s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))
# print(s.isAnagram("siva", "nisi"))