class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # 找到 #
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # 字符串从 j+1 开始，长度是 length
            word = s[j + 1 : j + 1 + length]
            res.append(word)

            # 跳到下一个 encoded string
            i = j + 1 + length

        return res