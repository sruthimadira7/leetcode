"""
Given two strings ransomNote and magazine, r
eturn true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #  store the length of the magazine
        m_len = len(magazine)
        r_len = len(ransomNote)

        #  check whether the length of ransomnote is greater than magazine
        #  if it is there is no way that one can construct
        #  ransomnote from Magazine
        if r_len > m_len:
            return False

        r_sorted = sorted(ransomNote)    
        m_sorted = sorted(magazine)

        i = 0
        j = 0

        while i < r_len and j < m_len:
            if r_sorted[i] == m_sorted[j]:
                i += 1
                j += 1
            elif r_sorted[i] > m_sorted[j]:
                j += 1     
            else:
                return False
            

        return i == r_len


s = Solution()
print(s.canConstruct("apple", "palealp"))  #true
print(s.canConstruct("apples", "palealp"))  #false