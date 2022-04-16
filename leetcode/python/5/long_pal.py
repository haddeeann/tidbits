import math


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        pal = s[0]
        longest = 1
        s_len = len(s)

        def testPalindrome(p):
            if len(p) % 2 == 0:
                # abcd
                i_right = int(len(p) / 2)
                i_left = i_right - 1
            else:
                # abc
                i = int(math.floor(len(p) / 2))
                i_right = i + 1
                i_left = i - 1

            while i_left >= 0 and i_right < len(p):
                if p[i_left] != p[i_right]:
                    return False
                i_left -= 1
                i_right += 1

            return True

        for i, letter in enumerate(s):
            j = i - 1
            k = i + 1
            word = s[i]
            while j >= 0 and k < s_len:
                word = s[j] + word + s[k]
                if testPalindrome(word) and len(word) > longest:
                    longest = len(word)
                    pal = word
                j -= 1
                k += 1

            if i > 0:
                j = i - 2
                k = i + 1
                word = s[i-1] + s[i]
            else:
                j = i - 1
                k = i + 1
                word = s[i]

            if testPalindrome(word) and len(word) > longest:
                longest = len(word)
                pal = word
            while j >= 0 and k < s_len:
                word = s[j] + word + s[k]
                if testPalindrome(word) and len(word) > longest:
                    longest = len(word)
                    pal = word
                j -= 1
                k += 1

        return pal


sol = Solution()
sol.longestPalindrome(
    "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa")
# print(sol.longestPalindrome("azwdzwmwcqzgcobeeiphemqbjtxzwkhiqpbrprocbppbxrnsxnwgikiaqutwpftbiinlnpyqstkiqzbggcsdzzjbrkfmhgtnbujzszxsycmvipjtktpebaafycngqasbbhxaeawwmkjcziybxowkaibqnndcjbsoehtamhspnidjylyisiaewmypfyiqtwlmejkpzlieolfdjnxntonnzfgcqlcfpoxcwqctalwrgwhvqvtrpwemxhirpgizjffqgntsmvzldpjfijdncexbwtxnmbnoykxshkqbounzrewkpqjxocvaufnhunsmsazgibxedtopnccriwcfzeomsrrangufkjfzipkmwfbmkarnyyrgdsooosgqlkzvorrrsaveuoxjeajvbdpgxlcrtqomliphnlehgrzgwujogxteyulphhuhwyoyvcxqatfkboahfqhjgujcaapoyqtsdqfwnijlkknuralezqmcryvkankszmzpgqutojoyzsnyfwsyeqqzrlhzbc"))
