class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for i in nums:
            dictionary[i] = dictionary.get(i, 0) + 1
        sorted_dict = sorted(dictionary.items(), key=lambda x: x[1],reverse=True)
        res = []
        for j in range(k):
            res.append(sorted_dict[j][0])

        return res