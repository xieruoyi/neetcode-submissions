class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        left = 0
        right = k - 1

        max_window = float("-inf")
        max_idx = -1

        while right < len(nums):

            # 如果当前最大值已经滑出窗口，就重新找最大值
            if left > max_idx:
                max_window = float("-inf")
                for i in range(left, right + 1):
                    if nums[i] >= max_window:
                        max_window = nums[i]
                        max_idx = i

            # 如果新进来的 right 比当前最大值大，更新最大值
            elif nums[right] >= max_window:
                max_window = nums[right]
                max_idx = right

            # 每个窗口只 append 一次
            res.append(max_window)

            left += 1
            right += 1

        return res