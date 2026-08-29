class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))

            else:
                right = stack.pop()
                left = stack.pop ()

                if i == "+":
                    result = left + right

                elif i =="-":
                    result = left - right

                elif i =="*":
                    result = left * right

                elif i =="/":
                    result = int(left / right)
            
                stack.append(result)

        return stack[-1]



                

              

                





               


