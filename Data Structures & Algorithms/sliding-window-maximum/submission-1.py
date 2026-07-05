from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for right in range(len(nums)):

            # 把比 nums[right] 小的都踢掉
            while q and nums[q[-1]] <= nums[right]:
                q.pop()

            q.append(right)

            # 如果队头已经不在窗口里，踢掉
            if q[0] <= right - k:
                q.popleft()

            # 从第一个完整窗口开始记录答案
            if right >= k - 1:
                res.append(nums[q[0]])

        return res