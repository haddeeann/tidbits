# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        for x in range(1, n+1):
            if x % 3 == 0 and x % 5 == 0:
                answer.append("FizzBuzz")
            elif x % 3 == 0:
                answer.append("Fizz")
            elif x % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(x))

        return answer


s = Solution()
s.fizzBuzz(15)