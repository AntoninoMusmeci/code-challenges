#https://leetcode.com/problems/baseball-game/description/
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        # next_record = 0
        for op in operations:
            if op == "+":
                records.append(records[-1] + records[-2])

            elif op == 'D':
                records.append(records[-1] * 2)

            elif op == 'C':
                records.pop()
            else:
                records.append(int(op))
        return sum(records)
