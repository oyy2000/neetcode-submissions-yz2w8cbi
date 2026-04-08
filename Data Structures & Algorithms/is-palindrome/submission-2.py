class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Reverse String
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        print(newStr)
        return newStr == newStr[::-1]