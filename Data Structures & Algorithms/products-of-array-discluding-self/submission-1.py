class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = []
        end = []
        front.append(nums[0]) # 1
        end.append(nums[-1]) # 6
        # front: 4 12 24 24 48
        # end: 2 2 4 12 48
        for i in range(1, len(nums)):
            front.append(front[i-1] * nums[i])
            end.append(end[i-1] * nums[len(nums) - i - 1])
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(end[len(nums)-2])
            elif i == len(nums) - 1:
                res.append(front[i-1])
            else:
                res.append(end[len(nums)-i-2]*front[i-1])
        return res