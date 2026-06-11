"""
Given a string num which represents an integer, return true if num is a strobogrammatic number.
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:
Input: num = "69"
Output: true

Example 2:
Input: num = "88"
Output: true

Example 3:
Input: num = "962"
Output: false

Constraints:
1 <= num.length <= 50
num consists of only digits.
num does not contain any leading zeros except for zero itself.
"""
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        inverse_char = {
            "0":  "0",
            "1":  "1",
            "6":  "9",
            "8":  "8",
            "9":  "6",
        }

        left = 0
        right = len(num) - 1

        while left <= right:
            if num[right] not in inverse_char or num[left] != inverse_char[num[right]]:
                return False
            
            left += 1
            right -= 1

        return True




s = Solution()
print(s.isStrobogrammatic("962"))
print(s.isStrobogrammatic("88"))
print(s.isStrobogrammatic("69"))