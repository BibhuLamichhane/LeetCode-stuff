class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        while len(tokens) > 1:
            try:
                a = int(tokens[i])
                b = int(tokens[i + 1])
                c = tokens[i + 2]
                if c in '+-/*':
                    if c == '+':
                        temp = a + b
                        tokens[i] = temp
                        tokens.pop(i + 1)
                        tokens.pop(i + 1)
                        i = 0
                    elif c == '-':
                        temp = a - b
                        tokens[i] = temp
                        tokens.pop(i + 1)
                        tokens.pop(i + 1)
                        i = 0
                    elif c == '*':
                        temp = a * b
                        tokens[i] = temp
                        tokens.pop(i + 1)
                        tokens.pop(i + 1)
                        i = 0
                    else:
                        temp = a / b
                        tokens[i] = temp
                        tokens.pop(i + 1)
                        tokens.pop(i + 1)
                        i = 0
                else:
                    i += 1
            except:
                i += 1
        return int(tokens[0])