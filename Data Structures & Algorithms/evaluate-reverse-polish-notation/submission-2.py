class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if (len(tokens) <= 2):
            return tokens[0]
        stack = [int(tokens[0])]
        operators = set(['+', '-','*','/'])
        for i in range(1, len(tokens)):
            print(stack)
            if (tokens[i] not in operators):
                stack.append(int(tokens[i]))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                #perform operation and save to num1
                if (tokens[i] == '+'):
                    stack.append(int(num1) + int(num2))
                elif (tokens[i] == '-'):
                    stack.append(int(num1) - int(num2))
                elif (tokens[i] == '*'):
                    stack.append(int(num1) * int(num2))
                elif (tokens[i] == '/'):
                    stack.append(int(num1 / num2))
                
        return stack[0]