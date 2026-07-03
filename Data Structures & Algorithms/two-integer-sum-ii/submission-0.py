class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        length = len(numbers)
        while i < length:
            j = i + 1
            while j < length:
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
                elif numbers[i] + numbers[j] > target:
                    break
                else:
                    j += 1
            i += 1