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

        # initialize an empty list to store reversed words
        rev_s = []

        # iterate through each word in the list
        for i in range(len(strs)):
            word = strs[i]

            # initialize an empty string to build the reversed word
            chars = []

            # iterate the word in reverse and append each character
            for j in range(len(word) - 1, -1, -1):
                chars.append(word[j])

            # join chars into a string and append to rev_s
            rev_s.append("".join(chars))

        # join the reversed words with a space and return
        return " ".join(rev_s)



s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))