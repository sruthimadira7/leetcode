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

        #  a hashmap that contains all its characters and their respective frequencies
        m_map = {}

        #  iterate the string magazine
        for i in range(m_len):
            #  store it's keys and values & update them each time
            m_map[magazine[i]] = m_map.get(magazine[i], 0) + 1

        #  iterate the ransomNote string
        for i in range(r_len):
            #  check if the character is in m_map or not
            #  check if it's value is 0 or not
            if ransomNote[i] not in m_map or m_map[ransomNote[i]] == 0:
                return False
            
            # decrement each time when we encounter the value
            m_map[ransomNote[i]] -= 1

        return True


s = Solution()
print(s.canConstruct("apple", "palealp"))  #true
print(s.canConstruct("apples", "palealp"))  #false