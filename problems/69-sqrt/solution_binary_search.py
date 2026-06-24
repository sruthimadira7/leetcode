"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Constraints:
0 <= x <= 231 - 1
"""
class Solution:
    def mySqrt(self, x: int) -> int:

        # if the input value is less than 2
        if x < 2:
        # it's squareroot is itself
            return x
        
        # initialize left to 2 nad right to half of the given input x
        left = 2
        right = x // 2

        # Check the condition if left is less than or equal to right for each iteration
        while left <= right:
            # compute mid each time
            mid = (left + right) // 2

            # calculate the square root
            sqrt = mid * mid
            # check if sqrt is equal to the given input x 
            if sqrt == x:
                # if it is return mid
                return mid
            # if the sqrt is greater than the given input
            elif sqrt > x:
                # move the right pointer to mid - 1
                right = mid - 1
            # if the sqrt is lesser than the given input
            else:
                # move the left pointer to mid + 1
                left = mid + 1

        return left - 1




s = Solution()
print(s.mySqrt(8))
print(s.mySqrt(4))
print(s.mySqrt(84))