from collections import deque

stack = deque()

#  valid parenthesis
def valid_parenthesis(s):
    ps_match = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }

    for i in s:
        print(i)
        if i in ps_match:
            stack.append(i)
        elif i in ps_match.values():
            if ps_match[stack.pop()] != i:
                return False
            
    return True if len(stack) == 0 else False

s = ""
print(valid_parenthesis(s))

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2:
            return False
            
        stack = []
        ps_match = {'(' : ')','[' : ']','{' : '}'}
        for i in s:
            if i in ps_match:
                stack.append(i)
            elif i in ps_match.values():
                if len(stack) == 0:
                    return False
                if ps_match[stack.pop()] != i:
                    return False
                
        return True if len(stack) == 0 else False
        