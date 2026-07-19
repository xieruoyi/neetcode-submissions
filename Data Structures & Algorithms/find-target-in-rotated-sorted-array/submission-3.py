class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]: # Left is ordered
                if target < nums[mid] and target >= nums[l]: # Target is in the left
                    r = mid - 1
                elif target < nums[mid] and target < nums[l]:
                    l = mid + 1
                elif target > nums[mid]:
                    l = mid + 1
            if nums[r] >= nums[mid]: # Right is ordered
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                elif target > nums[mid] and target > nums[r]:
                    r = mid - 1

        return -1