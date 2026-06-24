"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.


Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.
"""
class Solution:
    def reverseString(self, s: list[str]) -> None:
        # initialize left and right pointers at both ends of the array
        left = 0
        right = len(s) - 1

        while left < right:
            # swap the characters at left and right pointers
            s[left], s[right] = s[right], s[left]
            # move left pointer forward
            left += 1
            # move right pointer backward
            right -= 1

        return s


s = Solution()
print(s.reverseString(["H","a","n","n","a","h"]))
        