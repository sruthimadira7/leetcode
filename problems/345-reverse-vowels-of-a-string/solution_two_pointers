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
    def reverse_vowels(strs):
        strs_list = list(strs)
        print(strs_list)
        left = 0
        right = len(strs_list) - 1
        vowels_set = {"a", "e", "i", "o", "u"}

        while left < right:
            if strs_list[left] in vowels_set and strs_list[right] in vowels_set:
                strs_list[left], strs_list[right] = strs_list[right], strs_list[left]
                left += 1
                right -= 1
            elif strs[left] not in vowels_set:
                left += 1
            else:
                right -= 1

        return "".join(strs_list)
    
s = Solution()
print(s.reverse_vowels("hello"))
print(s.reverse_vowels("leetcode"))
