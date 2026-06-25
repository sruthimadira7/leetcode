"""
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.

Example 1:
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:
Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

Constraints:
1 <= num <= 231 - 1
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # handle edge case where num is 1
        if num == 1:
            return True

        # iterate from 2 to num // 2 + 1
        for i in range(2, num // 2 + 1):
            # check if i * i equals num
            if num == i * i:
                # if it is, num is a perfect square
                return True
        
        # if no perfect square found, return False
        return False


s = Solution()
print(s.isPerfectSquare(16))
print(s.isPerfectSquare(14))
print(s.isPerfectSquare(144))
print(s.isPerfectSquare(2000105819))