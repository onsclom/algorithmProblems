# Valid Parenthesis
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def convertRight(self, s: str) -> str:
        if s == "}":
            return "{"
        elif s == ")":
            return "("
        elif s == "]":
            return "["
    
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if (i == "{" or i == "[" or i == "("):
                stack += i
            else:
                if (len(stack)==0 or stack.pop() != self.convertRight(i)):
                    return 0
        
        if len(stack) == 0:
            return 1
        else:
            return 0