class Solution:
    def isPalindrome(self, s: str) -> bool:

        string = "".join(s.split()).lower()
        l, r = 0, len(string)-1

        while l < r:
            while l < r and not string[l].isalnum():
                l += 1
            while l < r and not string[r].isalnum():
                r -= 1
            if string[l] != string[r]:
                return False
            l, r = l+1, r-1
        return True


            
        print(string)