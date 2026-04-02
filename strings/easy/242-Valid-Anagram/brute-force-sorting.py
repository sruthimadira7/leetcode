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

        # Check whether both the strings have the same length
        # If lengths differ, no need to sort — return early
        
        if len(s) != len(t):
            return False
        
        # Sort both strings alphabetically.
        # Two strings are anagrams if and only if
        # their sorted forms are identical.
        # sorted() returns a list of chars.
        return sorted(s) == sorted(t)
    

s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))
# print(s.isAnagram("siva", "nisi"))