"""
1347. Minimum Number of Steps to Make Two Strings Anagram
You are given two strings of the same length s and t. 
In one step you can choose any character of t and replace it with another character.
Return the minimum number of steps to make t an anagram of s.
An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 

Constraints:
1 <= s.length <= 5 * 104
s.length == t.length
s and t consist of lowercase English letters only.
"""
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        print(s, t)
        num_steps = 0
        n = len(s)

        s_sorted = sorted(s)
        t_sorted = sorted(t)
        print(s_sorted)
        print(t_sorted)

        if s_sorted == t_sorted:
            return num_steps
        else:
            i = j = 0
            while i < n and j < n:
                if s_sorted[i] > t_sorted[j]:
                    j += 1
                elif s_sorted[i] < t_sorted[j]:
                    i += 1
                    num_steps += 1
                else:
                    i += 1
                    j += 1

        return num_steps + (n - i)


s = Solution()
print(s.minSteps("bab", "aba"))
print(s.minSteps("leetcode", "practice"))
print(s.minSteps("anagram", "mangaar"))
print(s.minSteps("friend", "family"))