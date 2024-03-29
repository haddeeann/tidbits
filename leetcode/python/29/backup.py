class Solution(object):
    def find_a(self, dividend, divisor):
        k = 0
        a = 0
        counter = divisor
        if divisor % 2 == 0:
            answer = dividend
            while divisor > 0:
                answer = answer >> 1
                divisor -= 2
            a = answer
        else:
            while counter < dividend:
                a += 1
                counter += divisor
        print(a)
        return a

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # limits
        neg_limit = -2**31
        pos_limit = 2**31 - 1
        # negative tester
        neg_divisor = divisor < 0
        neg_dividend = dividend < 0
        # set limits
        if dividend > pos_limit:
            dividend = pos_limit
        elif dividend < neg_limit:
            dividend = neg_limit
        # get absolute values
        divisor = abs(divisor)
        dividend = abs(dividend)
        # anything divided by itself is 1
        if divisor == dividend:
            a = 1
        elif divisor == 1:
            a = dividend
        else:
            a = self.find_a(dividend, divisor)
        if (neg_divisor and not neg_dividend) or (not neg_divisor and neg_dividend):
            a = -abs(a)
        if a > pos_limit:
            a = pos_limit
        elif a < neg_limit:
            a = neg_limit
        print(a)
        return a


sol = Solution()
# sol.find_a(2147483647, 2)
sol.find_a(12, 4)