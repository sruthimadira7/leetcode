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

        #  initialize a freq_map {}
        counter = {}

        # iterate the array
        for i in range(r_len):
            #  check the last occurred index of the character
            j = counter.get(ransomNote[i], 0)
            #  check whether the value of j is less than magazine's length or not
            while j < m_len:
                #  check whether if the characters at their respective indices matches
                if ransomNote[i] == magazine[j]:
                    # update the counter hashmap
                    #  with the next index
                    counter[ransomNote[i]] = j + 1
                    #  once we found the character
                    #  move to the next character
                    break

                j += 1

            #  Edge Case: If in any case the value of j is equal to magazine's length
            #  It meant we did not find that character in the magazine string
            if j == m_len:
                return False

        #  made it to here, which means we can construct
        #  RansomNote from Magazine
        return True
    

s = Solution()
print(s.canConstruct("a", "b"))  #false
print(s.canConstruct("a", "b"))  #false
print(s.canConstruct("aa", "aab"))  #true