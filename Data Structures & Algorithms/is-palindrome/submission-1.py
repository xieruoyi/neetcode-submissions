class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward_str = ""
        back_str = ""
        for i in range(len(s)):
            if 65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122 or 48 <= ord(s[i]) <= 57 :
                forward_str = s[i].lower() + forward_str
                back_str = back_str + s[i].lower()
            else:
                continue
        if back_str == forward_str:
            return True
        else:
            return False
            