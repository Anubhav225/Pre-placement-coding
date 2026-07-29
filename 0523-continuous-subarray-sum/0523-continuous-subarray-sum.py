class Solution:
    def checkSubarraySum(self, nums, k):
        remainder_index = {0: -1}
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            remainder = total % k

            if remainder in remainder_index:
                if i - remainder_index[remainder] >= 2:
                    return True
            else:
                remainder_index[remainder] = i

        return False