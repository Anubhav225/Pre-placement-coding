class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        arr = [(nums[i], i) for i in range(n)]

        def merge_sort(left, right):
            if left >= right:
                return

            mid = (left + right) // 2

            merge_sort(left, mid)
            merge_sort(mid + 1, right)

            temp = []
            i = left
            j = mid + 1
            right_count = 0

            while i <= mid and j <= right:
                if arr[j][0] < arr[i][0]:
                    temp.append(arr[j])
                    right_count += 1
                    j += 1
                else:
                    answer[arr[i][1]] += right_count
                    temp.append(arr[i])
                    i += 1

            while i <= mid:
                answer[arr[i][1]] += right_count
                temp.append(arr[i])
                i += 1

            while j <= right:
                temp.append(arr[j])
                j += 1

            for k in range(len(temp)):
                arr[left + k] = temp[k]

        merge_sort(0, n - 1)

        return answer