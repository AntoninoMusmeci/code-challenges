class Solution:
    def solveEquation(self, equation: str) -> str:
        x = 0
        sum = 0
        number = ""
        operation = {"+": 1, "-": -1}
        sign, start = (1, 0) if equation[0] != "-" else (-1, 1)

        i = start
        equation += "+"
        while i < len(equation):
            if equation[i] != "+" and equation[i] != "-" and equation[i] != "=":
                number += equation[i]
            else:
                if len(number) > 0:
                    if number[-1] != "x":
                        sum += int(number) * sign
                    else:
                        x += int(number[:-1] if len(number) > 1 else 1) * sign
                if equation[i] == "=":
                    operation["+"] = -1
                    operation["-"] = 1
                    sign = -1
                else:
                    sign = operation[equation[i]]
                number = ""
            i += 1

        if x == 0 and sum == 0:
            return "Infinite solutions"
        if x == 0:
            return "No solution"
        else:
            return "x=" + str(sum//x * -1)
