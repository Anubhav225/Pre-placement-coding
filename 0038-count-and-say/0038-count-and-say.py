class Solution:
    def countAndSay(self, n: int) -> str:
        answer = "1"

        for _ in range(n - 1):
            current = ""
            count = 1

            for i in range(len(answer)):
                if i + 1 < len(answer) and answer[i] == answer[i + 1]:
                    count += 1
                else:
                    current += str(count)
                    current += answer[i]
                    count = 1

            answer = current

        return answer