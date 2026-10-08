class Solution:
    def calPoints(self, operations: List[str]) -> int:


        current = []
        for i in operations:
            if  i == "+":
                score = current[-2] + current[-1]
                current.append(score)
            elif i == "D":
                current.append(2*current[-1])
            elif i == "C":
                current.remove(current[-1])
            else:
                current.append(int(i))
            print(current)
        return sum(current)


        