"""
A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains every letter of the English alphabet at least once.

Example 2:
Input: sentence = "leetcode"
Output: false

Constraints:
1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        #  check the length of the string less than 26
        #  if it is, it is not an Pangram
        if len(sentence) < 26:
            return False
        
        # take a string containing all the english lowercase letters
        temp = "abcdefghijklmnopqrstuvwxyz"
        # initialize a hash_map that stores the letters frequency
        temp_map = {}

        #  iterate the temp
        for ch in temp:
            # generate a hash_map containing all letters
            # make their count as 0
            temp_map[ch] = 0

        # itearte the given sentence
        for ch in sentence:
            #  increament the character count by 1 each time
            temp_map[ch] += 1
        
        # iterate the temp_map using temp_map.values()
        for val in temp_map.values():
            # if any of their values is equal to 'zero'
            if val == 0:
                #  it's not a Panagram
                return False
            
        # If it contains all the letters atleast once
        #  It's a Panagram
        return True


s = Solution()
print(s.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(s.checkIfPangram("leetcode"))