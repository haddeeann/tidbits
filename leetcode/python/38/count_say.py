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
            count = 1
            while len(test) > 0:
                first = test[:1]
                test = test[1:]
                while len(test) > 0 and first == test[0]:
                    count += 1
                    test = test[1:]
                add += str(count) + first
            counter += 1
            build = add
        return build


input = 4
sol = Solution()
answer = sol.countAndSay(input)
print(answer == "1211")