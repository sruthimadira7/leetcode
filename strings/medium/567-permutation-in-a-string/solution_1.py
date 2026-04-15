"""
567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # stores the lengths of both the strings
        n = len(s1)
        m = len(s2)

        # check whether the length of s2 is less than s1
        # return false
        if m < n:
            return False 
        
        # sort the string s1
        sorted_s1 = ''.join(sorted(s1))

        #  initialize pointers that keeps tract of the combination
        #  start and end
        i = 0
        j = n - 1

        # iterate the string s2
        while j < m:
            # slice the string s2 
            #  based on the start and end points
            slice_s2 = s2[i: j + 1]
            # sort the slice
            sorted_slice_s2 = ''.join(sorted(slice_s2))

            #  compare the sorted slice
            if sorted_slice_s2 == sorted_s1:
                # if both the slices are equal even for once,
                # return true since 
                # s1's permutations is the substring of s2
                return True
            
            #  increment the pointers each time
            i += 1
            j += 1

        # s1's permutations are not the substring of s2
        return False


s = Solution()
print(s.checkInclusion("ab", "eidbaooo")) # True
print(s.checkInclusion("ab", "eidboaoo")) # False



# problem: 567-permutation-in-a-string
# time complexity: 
# space complexity: 