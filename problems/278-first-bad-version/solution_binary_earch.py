"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1

Constraints:
1 <= bad <= n <= 231 - 1
"""
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# simulate the first bad version for local testing
bad_version = 4

def isBadVersion(version: int) -> bool:
    # all versions >= bad_version are considered bad
    return version >= bad_version


class Solution:
    def firstBadVersion(self, n: int) -> int:
        # initialize left and right boundaries
        left = 1
        right = n

        while left <= right:
            # compute mid to avoid integer overflow
            mid = (left + right) // 2

            if isBadVersion(mid):
                # mid is bad, but it could be the first bad version
                # so search the left half
                right = mid - 1
            else:
                # mid is good, first bad version must be to the right
                left = mid + 1

        # left is the first index where isBadVersion returns True
        return left


s = Solution()
print(s.firstBadVersion(5))   # Expected: 4
print(s.firstBadVersion(10))  # Expected: 4

# update bad_version to test a different scenario
bad_version = 1
print(s.firstBadVersion(1))   # Expected: 1