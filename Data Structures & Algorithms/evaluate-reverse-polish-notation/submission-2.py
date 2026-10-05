class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def is_numeric(num):
            try:
                float(num)
                return True
            except ValueError as e:
                return False
        
        for token in tokens:
            if is_numeric(token):
                stack.append(int(token))
            if token == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            if token == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            if token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            if token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            
        return stack.pop()