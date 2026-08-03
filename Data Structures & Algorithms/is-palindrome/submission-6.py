class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "" # Instantiate the cleaned string

        for char in s: # Iterate through the string
            if char.isalnum(): # Checking that the index is on a true data point or letter
                cleaned += char.lower() # Converted to lower case to check for true palindrome and adding to the cleaned string

        rev = cleaned[::-1] # Reverse the string to compare the forward and backward version

        return rev == cleaned # Boolean expression to make sure that it is the same forward and backward(palindrome) and return true/false accordingly