import math


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
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

        def testSubstrings(search_word, longest_word):
            pal = ""

            # j = 0
            # k = 2
            # # test three letters aka single core
            # for letter_sw in search_word[1:]:
            #     while j >= 0 and k < sw_l:
            #         word = s[j] + letter_sw + s[k]
            #         if len(word) > longest_word:
            #             if testPalindrome(word):
            #                 longest_word = len(word)
            #                 pal = word
            #         j -= 1
            #         k += 1

            # test four letters aka double core
            if len(search_word) > 3:
                for i_index, letter_sw in search_word[2:]:
                    if search_word[i_index - 1] == letter_sw:
                        word = search_word[i_index - 1] + letter_sw
                        if len(word) > longest_word:
                            longest_word = len(word)
                            pal = word
                        j_index = i_index - 2
                        k_index = i_index + 1
                        while j_index >= 0 and k_index < len(search_word):
                            word = search_word[j_index] + word + search_word[k_index]
                            if len(word) > longest_word:
                                if testPalindrome(word):
                                    longest_word = len(word)
                                    pal = word
                            j_index -= 1
                            k_index += 1

            return pal

        longest = 0
        long_pal = s[0]
        for i, letter in enumerate(s):
            # find longest possible substring
            end_index = len(s) - 1
            if i != end_index:
                right_length = end_index - i
                left_length = i
                length = right_length if right_length < left_length else left_length
                substring = s[i - length: i + length + 1]
            else:
                substring = s[end_index - 1] + s[end_index]
            if len(substring) > longest:
                palindrome = testSubstrings(substring, longest)
            if len(palindrome) > longest:
                longest = len(palindrome)
                long_pal = palindrome

        print(long_pal)


sol = Solution()
sol.longestPalindrome("abba")
# print(sol.longestPalindrome("azwdzwmwcqzgcobeeiphemqbjtxzwkhiqpbrprocbppbxrnsxnwgikiaqutwpftbiinlnpyqstkiqzbggcsdzzjbrkfmhgtnbujzszxsycmvipjtktpebaafycngqasbbhxaeawwmkjcziybxowkaibqnndcjbsoehtamhspnidjylyisiaewmypfyiqtwlmejkpzlieolfdjnxntonnzfgcqlcfpoxcwqctalwrgwhvqvtrpwemxhirpgizjffqgntsmvzldpjfijdncexbwtxnmbnoykxshkqbounzrewkpqjxocvaufnhunsmsazgibxedtopnccriwcfzeomsrrangufkjfzipkmwfbmkarnyyrgdsooosgqlkzvorrrsaveuoxjeajvbdpgxlcrtqomliphnlehgrzgwujogxteyulphhuhwyoyvcxqatfkboahfqhjgujcaapoyqtsdqfwnijlkknuralezqmcryvkankszmzpgqutojoyzsnyfwsyeqqzrlhzbc"))
