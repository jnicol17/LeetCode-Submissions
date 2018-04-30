# Solution to LeetCode Problem 412: Fizz Buzz
# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
# For numbers which are multiples of both three and five output “FizzBuzz”.

# Example:
# n = 15,
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        L = []
        for i in range(1,n+1):
            # if i is a factor of 15 (3 and 5)
            if (i % 15 == 0):
                L.append("FizzBuzz")
            # factor of 3
            elif (i % 3 == 0):
                L.append("Fizz")
            # factor of 5
            elif (i % 5 == 0):
                L.append("Buzz")
            # regular number
            else:
                L.append(str(i))
        return L
