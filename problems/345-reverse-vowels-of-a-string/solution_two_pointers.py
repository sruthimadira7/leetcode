"""
Given a string s, reverse only the vowels in s and return the resulting string. 
The vowels are 'a', 'e', 'i', 'o', 'u', and they may appear in both lower and upper case. 
Every non-vowel character must remain at its original index.

Example 1:
Input:  s = "hello"
Output: "holle"
Explanation: The vowels are 'e' (index 1) and 'o' (index 4). Swapping them gives "holle"; 'h', 'l', 'l' stay put.

Example 2:
Input:  s = "leetcode"
Output: "leotcede"
Explanation: The vowels in order are e, e, o, e. Reversed they are e, o, e, e, placed back into the original vowel slots.

Example 3:
Input:  s = "xyz"
Output: "xyz"
Explanation: No vowels, so the string is unchanged.

Constraints:
1 <= s.length <= 10^5
s consists of printable ASCII characters.

Follow-up: Do it in a single pass with O(1) extra space. 
How would you generalize the solution so the "which characters get reversed" rule is a parameter rather than hardcoded vowels?
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        # convert string to list to allow in-place swapping
        strs = list(s)

        # initialize left and right pointers at both ends of the array
        l = 0
        r = len(strs) - 1

        # define a set of vowels for O(1) lookup
        vowels_set = {"a", "e", "i", "o", "u"}

        while l < r:
            # if both pointers point to vowels, swap them
            if strs[l] in vowels_set and strs[r] in vowels_set:
                strs[l], strs[r] = strs[r], strs[l]
                l += 1
                r -= 1
            # if left pointer is not a vowel, move it forward
            elif s[l] not in vowels_set:
                l += 1
            # if right pointer is not a vowel, move it backward
            else:
                r -= 1

        # join the list back into a string and return
        return "".join(strs)
    
s = Solution()
print(s.reverseVowels("hello"))
print(s.reverseVowels("leetcode"))
