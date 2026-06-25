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

        # initialize left and right boundaries
        left = 1
        right = num

        while left <= right:
            # compute mid for each iteration
            mid = (left + right) // 2

            # compute the square of mid
            square = mid * mid

            if square == num:
                # mid is the perfect square root of num
                return True
            elif square > num:
                # square is too large, search the left half
                right = mid - 1
            else:
                # square is too small, search the right half
                left = mid + 1

        # no perfect square found
        return False


s = Solution()
print(s.isPerfectSquare(16))
print(s.isPerfectSquare(14))
print(s.isPerfectSquare(144))
print(s.isPerfectSquare(2000105819))