class Solution:
    def runningSum(self, nums):
        total = 0
        answer = []

        for num in nums:
            total += num
            answer.append(total)

        return answer