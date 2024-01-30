class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        :type current int
        """
        if n == 1:
            return n
        counter = 1
        build = ''
        while counter < n:
            if build == '':
                test = str(counter)
            else:
                test = build
            add = ''
            while len(test) > 0:
                count = 1
                first = test[:1]
                test = test[1:]
                if test != '':
                    while first == test[0]:
                        count += 1
                        test = test[1:]
                        if test == '':
                            break
                add += str(count) + first
            build = add
            counter += 1


input = 4
sol = Solution()
sol.countAndSay(input)