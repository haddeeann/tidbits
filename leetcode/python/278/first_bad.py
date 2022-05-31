# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
import math
def isBadVersion(num):
    bad = 2
    if num >= bad:
        return True
    else:
        return False


def isFirstBadVersion(num):
    if isBadVersion(num) and not isBadVersion(num - 1):
        return True
    else:
        return False


def findNewRange(range):
    new_range = {}
    lower = range["lower"]
    mid = range["mid"]
    upper = range["upper"]
    if isBadVersion(mid) and isBadVersion(mid - 1):
        if mid - 1 == lower:
            new_range["lower"] = lower
            new_range["upper"] = mid
            new_range["mid"] = lower
        else:
            # go left
            new_range["lower"] = lower
            new_range["upper"] = mid
            new_range["mid"] = lower + math.floor((upper - lower) / 2)
    else:
        if mid + 1 == upper:
            new_range["lower"] = mid
            new_range["upper"] = upper
            new_range["mid"] = upper
        else:
            # go right
            new_range["lower"] = mid
            new_range["upper"] = upper
            new_range["mid"] = lower + math.floor((upper - lower) / 2)

    return new_range

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        answer = None
        test = math.floor(n / 2) if n > 1 else n
        test_range = {
            "lower": 1,
            "mid": test,
            "upper": n
        }

        while answer is None:
            if isFirstBadVersion(test_range["mid"]):
                answer = int(test_range["mid"])
            else:
                test_range = findNewRange(test_range)

        return answer


sol = Solution()
sol.firstBadVersion(2)