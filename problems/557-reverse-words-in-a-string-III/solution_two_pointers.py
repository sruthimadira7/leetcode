"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "Mr Ding"
Output: "rM gniD"

Constraints:
1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        # split the string by whitespace into a list of words
        strs = s.split()

        # iterate through each word in the list
        for i in range(len(strs)):
            # convert the word into a list of characters for in-place swapping
            word = list(strs[i])

            # initialize left and right pointers at both ends of the word
            left = 0
            right = len(word) - 1

            while left < right:
                # swap the characters at left and right pointers
                word[left], word[right] = word[right], word[left]
                # move left pointer forward
                left += 1
                # move right pointer backward
                right -= 1

            # join the reversed characters back into a string and update the list
            strs[i] = "".join(word)

        # join the reversed words with a space and return
        return " ".join(strs)



s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))