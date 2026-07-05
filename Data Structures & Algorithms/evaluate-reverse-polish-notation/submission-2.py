class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        temp = 0
        for i in range(len(tokens)):
            if tokens[i] == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                temp = val1 + val2
                stack.append(temp)
            
            elif tokens[i] == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                temp = val2 - val1
                stack.append(temp)


            elif tokens[i] == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                temp = val1 * val2
                stack.append(temp)

            elif tokens[i] == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                temp = int(val2 / val1)
                stack.append(temp)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]