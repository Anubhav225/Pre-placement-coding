class Solution:
    def minWindow(self, s, t):
        need = {}
        window = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        left = 0
        matched = 0
        start = 0
        min_len = float("inf")

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                matched += 1

            while matched == len(need):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    matched -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]