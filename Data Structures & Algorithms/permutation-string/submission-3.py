class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)

        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:window])

        if s1_count == window_count:
            return True

        for right in range(window, len(s2)):
            left = right - window

            # add new right char
            window_count[s2[right]] += 1

            # remove old left char
            window_count[s2[left]] -= 1

            # delete key if count becomes 0
            if window_count[s2[left]] == 0:
                del window_count[s2[left]]

            if window_count == s1_count:
                return True

        return False