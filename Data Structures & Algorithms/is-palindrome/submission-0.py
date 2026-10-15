class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = "".join([letter for letter in s if letter.isalnum()]).lower()
        return stripped == stripped[::-1]
