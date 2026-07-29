class Solution:
    def subarraySum(self, nums, k):
        sums = {0: 1}
        total = 0
        answer = 0

        for num in nums:
            total += num

            if total - k in sums:
                answer += sums[total - k]

            sums[total] = sums.get(total, 0) + 1

        return answer