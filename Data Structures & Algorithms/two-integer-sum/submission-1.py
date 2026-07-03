class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tuple_lists = []

        for idx, num in enumerate(nums):
            tuple_lists.append((num, idx))

        tuple_lists_sorted = sorted(tuple_lists, key=lambda x: x[0])

        n = len(tuple_lists_sorted)

        for i in range(n):
            for j in range(i + 1, n):
                curr_sum = tuple_lists_sorted[i][0] + tuple_lists_sorted[j][0]

                if curr_sum == target:
                    return [min(tuple_lists_sorted[i][1], tuple_lists_sorted[j][1]),max(tuple_lists_sorted[i][1], tuple_lists_sorted[j][1])]
                elif curr_sum > target:
                    break