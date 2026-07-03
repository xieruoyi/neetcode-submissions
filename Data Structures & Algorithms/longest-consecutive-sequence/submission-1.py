class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        long = 1
        seen = set()
        for i in nums:
            seen.add(i)
        for i in nums:
            res = 1
            while i-1 in seen:
                i -= 1
            start = i
            while start + 1  in seen:
                res += 1
                start += 1
            long = max(long, res)
        return long