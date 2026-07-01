class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for char in s:
            if char.isalnum():
                cleaned += char.lower() # If the character is a letter then make it lower and append to new string 
        
        rev = cleaned[::-1] # Reverse string post-clean

        return rev == cleaned #return both being equal == true or false if not