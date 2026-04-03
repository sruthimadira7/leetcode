"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:
Input: s = "f11", t = "b23"
Output: false

Explanation:
The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # Check whether the length of the two strings same or not
        #  If different, they can never be Isomorphs
        if len(s) != len(t):
            return False
        
        #  store the length of any given string in a variable
        n = len(s)
        #  a hashmap to map the characters of two strings
        mapping_s_to_t = {}
        mapping_t_to_s = {}

        #  Iterate any one of the string
        for i in range(n):
            if (s[i] in mapping_s_to_t and mapping_s_to_t[s[i]] != t[i]) or (
                t[i] in mapping_t_to_s and mapping_t_to_s[t[i]] != s[i]):
                return False

            mapping_s_to_t[s[i]] = t[i]
            mapping_t_to_s[t[i]] = s[i]

        return True
    

s = Solution()
print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("paper", "title"))
print(s.isIsomorphic("paperssss", "titlesese"))
print(s.isIsomorphic("f11", "a23"))