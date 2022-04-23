class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        random_a = 4
        random_b = 5
        add_3 = random_a & random_b
        # lower_limit = -(2 ** 31)
        # upper_limit = (2 ** 31) - 1
        print("{0:b}".format(random_a))
        print("{0:b}".format(random_b))
        print("{0:b}".format(add_3))

        if add_3 == random_a and add_3 == random_b:
            print("same")
        else:
            print(add_3)


sol = Solution()
sol.reverse(123)