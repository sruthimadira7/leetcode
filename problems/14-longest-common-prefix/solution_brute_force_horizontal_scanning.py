"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Store the first word of the strs in longest_common_prefix
        longest_common_prefix = strs[0]

        # Traverse the entire array starting from index 1 to end sequentially
        for i in range(1, len(strs)):
            # store words at each index in a variable
            word = strs[i]
            # store the length of the longest_common_prefix in a variable
            k = len(longest_common_prefix)
            # store the length of the word of each iteration in variable
            j = len(word)
            # initialize a variable that keep tracks of the indices of both the words
            l = 0
            # check the condition whether i is less than both j & k
            while l < j and l < k :
                # check whether the characters at respective equal or not
                if word[l] != longest_common_prefix[l]:
                    # if they are not equal, thye don't match the prefix any further
                    break
                
                # for each iteration, increment the l by 1
                l += 1

            # update the index till the l since it matches the son common longest_common_prefix for each word
            longest_common_prefix = longest_common_prefix[:l]

            # for each iteration check whether the longest_common_prefix is empty or not
            if not longest_common_prefix:
                # if it's empty return early
                break
            

        return longest_common_prefix




s = Solution()
print(s.longestCommonPrefix(["dog","racecar","car"]))
print(s.longestCommonPrefix(["flower","flow","flight"]))