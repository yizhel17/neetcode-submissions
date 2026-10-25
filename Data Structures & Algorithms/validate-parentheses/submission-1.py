class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        match = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for cha in s:
            #right-ward
            if cha in match:
                stack.append(cha)
            else:
                #Left-ward
                if stack and match[stack[-1]] == cha:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
