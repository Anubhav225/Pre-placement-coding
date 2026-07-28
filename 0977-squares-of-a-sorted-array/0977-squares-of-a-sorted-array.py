class Solution:
    def sortedSquares(self, nums):
        left = 0
        right = len(nums) - 1
        ans = [0] * len(nums)
        i = len(nums) - 1

        while left <= right:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                ans[i] = nums[left] * nums[left]
                left += 1
            else:
                ans[i] = nums[right] * nums[right]
                right -= 1

            i -= 1

        return ans