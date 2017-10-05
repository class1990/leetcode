class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_str = ''
        max_len = 0
        for char in s:
            if char in sub_str:
                # take the sub_str after the same char as the pre_string for the next
                sub_str = sub_str[sub_str.index(char)+1::] + char
            else:
                sub_str += char
                max_len = max(max_len, len(sub_str))

        return max_len


if __name__ == '__main__':
    result = Solution().lengthOfLongestSubstring('pwwkew')
    print result