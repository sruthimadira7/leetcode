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
        # initialize an empty array
        s_arr = []

        # reverse traversal of the input array
        for i in range(len(s) -1, -1, -1):
            # append the current character to s_arr
            s_arr.append(s[i])

        return s_arr 


s = Solution()
print(s.reverseString(["H","a","n","n","a","h"]))
        