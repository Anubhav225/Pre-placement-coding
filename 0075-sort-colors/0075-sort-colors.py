class Solution:
    def sortColors(self, nums):
        zero = nums.count(0)
        one = nums.count(1)
        two = nums.count(2)

        i = 0

        while zero:
            nums[i] = 0
            i += 1
            zero -= 1

        while one:
            nums[i] = 1
            i += 1
            one -= 1

        while two:
            nums[i] = 2
            i += 1
            two -= 1