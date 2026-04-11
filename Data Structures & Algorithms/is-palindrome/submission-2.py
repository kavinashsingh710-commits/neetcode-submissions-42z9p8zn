class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_list = [char if char.isalnum() else '' for char in s ]
        string = "".join(str_list).lower()
        print(string)
        if string==string[::-1]:
            return True
        else:
            return False
        