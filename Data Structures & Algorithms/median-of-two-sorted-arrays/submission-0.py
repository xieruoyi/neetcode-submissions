class Solution:
    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> float:

        # 始终在较短的数组上做二分搜索
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        A = nums1
        B = nums2

        total = len(A) + len(B)
        half = (total + 1) // 2

        l = 0
        r = len(A)

        while l <= r:
            # i 和 j 表示左边分别放多少个元素
            i = (l + r) // 2
            j = half - i

            # 获取切割点左右的值
            A_left = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i] if i < len(A) else float("inf")

            B_left = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j] if j < len(B) else float("inf")

            # 找到正确切割
            if A_left <= B_right and B_left <= A_right:
                if total % 2 == 1:
                    return float(max(A_left, B_left))

                return (
                    max(A_left, B_left)
                    + min(A_right, B_right)
                ) / 2

            # A 左边元素太大，切割点向左
            elif A_left > B_right:
                r = i - 1

            # A 左边元素太少，切割点向右
            else:
                l = i + 1