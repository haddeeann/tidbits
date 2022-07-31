class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pattern = ''
        word_1 = ''
        word_2 = ''
        overall_min_length = None
        word_pattern = ''
        if len(strs) == 1:
            return strs[0]
        for i, word in enumerate(strs):
            if i != len(strs) - 1:
                word_1 = strs[i]
                word_2 = strs[i+1]
                short_word_length = min(len(word_1), len(word_2))
                if overall_min_length is None:
                    overall_min_length = short_word_length
                else:
                    overall_min_length = min(overall_min_length, short_word_length)
                if pattern == '' and i == 0:
                    for x in range(short_word_length):
                        if word_1[x] == word_2[x]:
                            pattern += word_1[x]
                        else:
                            break
                elif pattern != '':
                    overall_min_length = min(overall_min_length, len(pattern))
                    word_pattern = ''
                    for x in range(overall_min_length):
                        if word_1[x] == word_2[x] == pattern[x]:
                            word_pattern += word_1[x]
                        else:
                            break

                    if len(word_pattern) < len(pattern):
                        pattern = word_pattern

        return pattern

sol = Solution()
print(sol.longestCommonPrefix(["a","aca","accb","b"]))