"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? 
How would you adapt your solution to such a case?
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check whether both the strings have the same length
        # If lengths differ, they can never be anagrams
        if len(s) != len(t):
            return False
        
        # freq_map stores how many times each character
        # appears in t. We'll "spend" these counts against s.
        freq_map = {}

        # ── Phase 1: Build the frequency table from t ──────────────
        # For every character in t, increment its count.
        # If the char isn't in the map yet, default to 0 then add 1.
        for ch in t:
            freq_map[ch] = freq_map.get(ch, 0) + 1

        # ── Phase 2: Verify s uses exactly those characters ─────────
        # For every character in s, we try to "spend" one from the map.
        for ch in s:
            #  check whether the character at the current index is present in the hashmap or not
            #  also check whether the value of the character is 'zero'
            #  they are not anagrams
            if ch not in freq_map or freq_map[ch] == 0:
                return False
            
            # If the character is present and it's frequency is greater than 0 
            # Update it's frequency value by decrementing with 1 
            freq_map[ch] -= 1

        # All characters in s matched exactly with t's frequency table.
        # Every count is now 0 → it's a valid anagram.
        return True
    

s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))