class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        ans = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):

                x = ord(num1[i]) - ord("0")
                y = ord(num2[j]) - ord("0")

                total = x * y + ans[i + j + 1]

                ans[i + j + 1] = total % 10
                ans[i + j] += total // 10

        result = ""

        for digit in ans:
            if result == "" and digit == 0:
                continue
            result += str(digit)

        return result