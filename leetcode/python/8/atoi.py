import re


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        hex_lower = -0x80000000
        hex_upper = 0x7fffffff
        trimmed_s = s.strip()
        zero = 0
        answer_int = 0
        pos = True
        if trimmed_s == "":
            return answer_int
        if trimmed_s[0] == "-":
            pos = False
            trimmed_s = trimmed_s[1:]
        elif trimmed_s[0] == "+":
            trimmed_s = trimmed_s[1:]

        letter_index = re.search("[a-zA-Z\s\.\-\+]", trimmed_s)
        if letter_index is not None:
            end_index = letter_index.start()
            number_group = trimmed_s[:end_index]
        else:
            number_group = trimmed_s
        if not number_group.isdigit():
            return answer_int
        else:
            int_group = int(number_group) if pos else int("-" + number_group)
        if pos or int_group == zero:
            if int_group == int_group & hex_upper:
                answer_int = int_group
            else:
                return hex_upper
        else:
            if hex_lower == int_group & hex_lower:
                answer_int = int_group
            else:
                return hex_lower

        return answer_int


sol = Solution()
print(sol.myAtoi("  -0k4"))


