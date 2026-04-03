class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = sorted(s) # Sort both strings
        t_sorted = sorted(t)

        if s_sorted == t_sorted: # compare if strings match post sort
            return True # If they do then they are valid anagrams
        return False # If they don't match they aren't // return false