class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        stack = []

        for cha in tokens:
            if cha not in ["+", "-", "*", "/"]:
                stack.append(int(cha))
            
            elif cha == "+":
                b_val = stack.pop()
                a_val = stack.pop()

                new_val = ops[cha](a_val, b_val)

                stack.append(new_val)
            
            elif cha == "-":
                b_val = stack.pop()
                a_val = stack.pop()

                new_val = ops[cha](a_val, b_val)

                stack.append(new_val)
            
            elif cha == "*":
                b_val = stack.pop()
                a_val = stack.pop()

                new_val = ops[cha](a_val, b_val)

                stack.append(new_val)
            
            elif cha == "/":
                b_val = stack.pop()
                a_val = stack.pop()

                new_val = ops[cha](a_val, b_val)

                stack.append(new_val)
        
        return stack[-1]