class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # if x > 9 and (x % 10 == 0):
        #     return False
        digit = 0
        y = z = x
        while y >= 1:
            digit += 1
            y //= 10
        for i in range(digit//2):
            if ((x // (10**(digit-i-1))) % 10) != (z % 10):
                return False
            z //= 10
        return True