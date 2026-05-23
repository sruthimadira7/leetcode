"""
9. Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-2³¹ <= x <= 2³¹ - 1
Follow up: Could you solve it without converting the integer to a string?
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Condition 1: Negative numbers can't be palindromes (they have a "-" sign)
        # Condition 2: Numbers ending with 0 can't be palindromes (except 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        #  initialize reverse_x to "zero"
        reverse_x = 0

        # Keep reversing the second half of x until 
        # we've reversed half the digits
        while x > reverse_x:
            # Extract the last digit of x and add to reversed number
            #  build the reverted number
            reverse_x = reverse_x * 10 + x % 10
            # Remove the last digit from x
            x = x // 10

        # For even-length numbers (like 1221): x == reverse_x
        # For odd-length numbers x == reverse_x // 10
        return x == reverse_x or x == reverse_x // 10


s = Solution()
print(s.isPalindrome(1221))