class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                # 最小值一定在右半边
                l = mid + 1
            else:
                # 最小值在左半边（包括 mid）
                r = mid

        return nums[l]