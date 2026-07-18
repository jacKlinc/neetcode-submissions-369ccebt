class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # RPN is where the operands precede the operator
        # 12+ is the same as 1+2
        # could have a stack that is pushed onto until an operator is reached
        # apply operations to some variable when the stack is emptied
        stack = []
        for t in tokens:
            match t:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    op1, op2 = stack.pop(), stack.pop()
                    stack.append(op2 - op1)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    op1, op2 = stack.pop(), stack.pop()
                    stack.append(int(op2 / op1))
                case _:
                    stack.append(int(t))

        return stack[0]