# Solution for Leet Code Problem 344: Reverse String
# Write a function that takes a string as input and returns the string reversed.

# Example:
# Given s = "hello", return "olleh".

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # using extended list slicing to reverse the list in one line. 
        # More info here: https://docs.python.org/release/2.3.5/whatsnew/section-slices.html
        return s[::-1]
