"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

Constraints:
1 <= s.length <= 10⁵
s consists of lowercase English letters.
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1


        
                
                

s = Solution()
print(s.validPalindrome("cbbcc")) # True
print(s.validPalindrome("abc")) # False
print(s.validPalindrome("zryxeededexyz")) # False
print(s.validPalindrome("eceec")) # True