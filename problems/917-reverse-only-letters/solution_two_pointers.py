"""
Given a string s, reverse the string according to the following rules:
All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.


Example 1:
Input: s = "ab-cd"
Output: "dc-ba"

Example 2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
"""
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # convert string to list of characters for in-place swapping
        strs = list(s)

        # initialize left and right pointers at both ends of the array
        l = 0
        r = len(strs) - 1

        while l < r:
            # if both pointers point to letters, swap them
            if strs[l].isalpha() and strs[r].isalpha():
                strs[l], strs[r] = strs[r], strs[l]
                l += 1
                r -= 1
            else:
                # if left pointer is not a letter, move it forward
                if not strs[l].isalpha():
                    l += 1
                # if right pointer is not a letter, move it backward
                else:
                    r -= 1

        # join the list back into a string and return
        return "".join(strs)



s = Solution()
print(s.reverseOnlyLetters("a-bC-dEf-ghIj"))
print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!"))