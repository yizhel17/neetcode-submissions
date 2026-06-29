class Solution:
    def isValid(self, s: str) -> bool:
        Map = {"[": "]", "{": "}", "(": ")"}

        stack = []

        for cha in s:
            if cha in Map:
                stack.append(cha)
            else:
                if len(stack) != 0:
                    mat = stack[-1]
                    if Map[mat] == cha:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        return len(stack) == 0