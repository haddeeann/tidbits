class Solution(object):
    def romanToInt(self, str):
        """
        :type s: str
        :rtype: int
        """
        lookup = {
            'CM': 900,
            'M': 1000,
            'CD': 400,
            'D': 500,
            'XC': 90,
            'C': 100,
            'XL': 40,
            'L': 50,
            'IX': 9,
            'X': 10,
            'IV': 4,
            'V': 5,
            'I': 1
        }
        lc = ''
        skip_letter = False
        int_value = 0
        for i, s in enumerate(str):
            if skip_letter:
                skip_letter = False
                continue

            if i != len(str) - 1:
                lc = str[i] + str[i+1]
                if lookup.get(lc) is not None:
                    print(lc, lookup[lc])
                    int_value += lookup[lc]
                    skip_letter = True
                    continue

            if lookup.get(s) is not None:
                print(s, lookup[s])
                int_value += lookup[s]
                continue

        return int_value



sol = Solution()
s = "III"
a = 3
if sol.romanToInt(s) == a:
    print("test one passed")
else:
    print("test one failed")

s = "LVIII"
a = 58
if sol.romanToInt(s) == a:
    print("test two passed")
else:
    print("test two failed")

s = "MCMXCIV"
a = 1994
if sol.romanToInt(s) == a:
    print("test three passed")
else:
    print("test three failed")


