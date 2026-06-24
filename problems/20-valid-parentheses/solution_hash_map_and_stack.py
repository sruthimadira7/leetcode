"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        print(s)

        #  create a hashmap with the respective key and values as required
        pairs = {
            "(": ")",
            "{": "}", 
            "[":"]",
        }

        #  initialize an empty list in a variable
        stack = []

        # iterate the string
        for ch in s:
            #  check if the character is in pairs
            if ch in pairs:
                #  if it is present, append the character to the stack
                stack.append(ch)
            # if the character is not in pairs.keys()
            #  check if the character is present in pairs.values()
            elif ch in pairs.values():
                #  if the stack is empty or
                #  the last character popped from the stack value should be equal to the character
                if not stack or pairs[stack.pop()] != ch:
                    #  if not the given string is not a valid one
                    return False
        
        return len(stack) == 0



s = Solution()
print(s.isValid("([])"))
print(s.isValid("([)]"))