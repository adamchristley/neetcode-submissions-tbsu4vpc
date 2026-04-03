class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # You have two pointers, one from each direction of the string.
        # The first pointer i goes forward and the second pointer j goes backwards
        # via len(s) - 1. While i is less than j or you haven't ran through the whole list
        # continue iterating. Then you also check if it isn't a valid character with isalnum
        # increment. Now you are able to compare the lowercase (with .lower()) of s and j while iterating
        # return true/false dependant on if s and j are the same letter.

        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True
