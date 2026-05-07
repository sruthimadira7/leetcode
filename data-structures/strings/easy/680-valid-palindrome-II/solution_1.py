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
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                
                i += 1
                j -= 1
            
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[i]:
                return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
            
            i += 1
            j -= 1


        return True

s = Solution()
print(s.validPalindrome("cbbcc")) # True
print(s.validPalindrome("abc")) # False
print(s.validPalindrome("zryxeededexyz")) # False
# print(s.validPalindrome("eceec")) # True
print(s.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")) # True
# a g u o k e p a t g b n v f q m g m l c 