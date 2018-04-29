# Solution for LeetCode Problem 824: Goat Latin Translator
# Problem is part of weekly contest 82 and can be found here
# https://leetcode.com/contest/weekly-contest-82/problems/goat-latin/
#A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

#We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

#The rules of Goat Latin are as follows:

#If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
#For example, the word 'apple' becomes 'applema'.
 
#If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
#For example, the word "goat" becomes "oatgma".
 
#Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
#For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
#Return the final sentence representing the conversion from S to Goat Latin.

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        ans = ""
        # count is used to add whitespaces to after every word (except the last one) and to determine how many a's to add to the end
        count = 1;
        for word in S.split():
            # adding whitespace
            if count != 1:
                ans += " "
            # if the word starts with a vowel, we do not move the first letter
            if (word[0].lower() in ["a","e","i","o","u"]):
                ans += word + "ma" + count * "a"
            # if the word starts with a consonant, we move the first letter to the end
            else:
                ans += word[1:len(word)] + word[0] + "ma" + count * "a"
            count += 1
        return ans
