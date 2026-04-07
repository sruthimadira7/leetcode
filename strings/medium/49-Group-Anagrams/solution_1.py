"""
49. Group Anagrams
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        print(strs)
        # store the length of the list 
        strs_len = len(strs)
        # stores all the possible group of anagrams
        anagrams_list = []


        # iterate the list
        for i, curr_word in enumerate(strs):
                
            #  initialize a curr_word_char_freq_map {}
            curr_word_char_freq = {}
            #  iterate each word
            for ch in curr_word:
                #  update the curr_word_char_freq map
                curr_word_char_freq[ch] = curr_word_char_freq.get(ch, 0) + 1
            
            #  displays the curr_word_char_freq_map {}
            print(f'The current word \'{curr_word}\' freq map: {curr_word_char_freq}')
            # after creating the frequency map of the curr_word
            #  it doesn't matter, we have an anagram for it or not,
            # anyway it needs to be appended
            curr_word_anagrams = [curr_word]
            print(f'The current word anagrams initially: {curr_word_anagrams}')

            # iterate the list 
            for j in range(i + 1, strs_len):
                    word = strs[j]
                    #  displays the current word & the word to be compared
                    print(f'The Current word and the word to be compared are: {curr_word} & {word}')
                    # initialize a word_char_freq {}
                    word_char_freq = {}
                    #  iterate the word
                    for ch in word:
                        # update the word character frequenciess
                        word_char_freq[ch] = word_char_freq.get(ch, 0) + 1
                    
                    #  display the word character frequencies
                    print(f'The word \'{word}\' freq map: {word_char_freq}')

                    # two strings are said to be anagrams
                    # if they have same characters with same frequency
                    # which means first criteria to be checked is their lengths,
                    if len(curr_word_char_freq) == len(word_char_freq):
                        # initialize a variable to indicate whether
                        # the two words are being compared anagrams or not 
                        are_anagrams = True
                        #  iterate the curr_word_char_freq with .keys()
                        for key in curr_word_char_freq.keys():
                            #  check if any of the character frequencies differ
                            #  they are not anagrams
                            if curr_word_char_freq[key] != word_char_freq.get(key, 0):
                                are_anagrams = False
                                break
                        
                    if are_anagrams:
                        curr_word_anagrams.append(word)
                                
                    print(f'The current word anagrams are: {curr_word_anagrams}')
            
            anagrams_list.append(curr_word_anagrams)
            print(f'The grouped anagrasm are: {anagrams_list}')
            
        # return anagrams_list
        
        
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))