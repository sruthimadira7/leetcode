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
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # stores the lengths of both the strings
        n = len(s1)
        m = len(s2)

        # check whether the length of s2 is less than s1
        # return false
        if m < n:
            return False 
        
        # create a char_freq map for both the strings
        s1_count = Counter(s1)
        s2_count = Counter()

        #  iterate the string s2
        for i, ch in enumerate(s2):
            #  update each time the character frequencies of s2 string in s2_count
            s2_count[ch] = s2_count.get(ch, 0) + 1

            #  if the i value greater than n
            if i >= n:
                # check the count of ch 
                # at the index i - n 
                #  equal to 1 
                if s2_count[s2[i - n]] == 1:
                    #  if it is delete the key
                    del s2_count[s2[i - n]]
                else:
                    # if it is not decreement it's count by 1
                    s2_count[s2[i - n]] -= 1
            
            # check every single time 
            # their character frequencies equal or not
            if s1_count == s2_count:
                #  if it is
                # one of s1's permutations is the substring of s2
                return True
            
        # None of s1's permutations is the substring of s2
        return False
            

s = Solution()
print(s.checkInclusion("ab", "eidbaooo")) # True
print(s.checkInclusion("ab", "eidboaoo")) # False


# time complexity: 
# space complexity: 