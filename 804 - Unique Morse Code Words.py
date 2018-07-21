# Solution for LeetCode problem 804 - Unique Morse Code Words
# Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

# Return the number of different transformations among all words we have.

# Example:
# Input: words = ["gin", "zen", "gig", "msg"]
# Output: 2
# Explanation: 
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."

# There are 2 different transformations, "--...-." and "--...--.".

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # create a dictionary which maps lowercase letters to list indices of morse
        alpha = {
                "a" : 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,
                "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23,
                "y": 24, "z": 25}
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.",
                 "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # We use a set here because if we try to add an element that already exists, it will not add it
        morseSet = set([])
        # Gets reset for each word
        morseWord = ""
        for word in words:
            for letter in word:
                morseWord += morse[alpha[letter]]
            morseSet.add(morseWord)
            morseWord = ""
        return len(morseSet)
        
