"""
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). 
You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""
class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        #  store the length of the given list 
        words_len = len(words)

        # find out the minimum word in the given list
        min_word = min(words, key=len)

        #  construct a character frequency map
        min_word_char_freq = {}
        #  a list containing common characters to return
        common_char_list = []

        # iterate the min_word
        for ch in min_word:
            # update it's characters frequency each time
            min_word_char_freq[ch] = min_word_char_freq.get(ch, 0) + 1


        #  iterate the given list
        for word in words:
            #  iterate the list except for the min_word
            if word != min_word:
                current_freq_map = {}

                for ch in word:
                    current_freq_map[ch] = current_freq_map.get(ch, 0) + 1

                for ch, val in min_word_char_freq.items():
                    min_word_char_freq[ch] = min(min_word_char_freq[ch], current_freq_map.get(ch, 0))


        for ch, val in min_word_char_freq.items():
            if val > 0:
                for _ in range(val):
                    common_char_list.append(ch)  

        return common_char_list
        

s = Solution()
print(s.commonChars(["cool","lock","cook"]))
print(s.commonChars(["bella","label","roller"]))