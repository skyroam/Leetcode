class Solution:
    def reverse(self, x: int) -> int:
        lis = str(x)
        if lis[0] == '-':
            result = -int(lis[:0:-1])
            if result < -(1<<31):
                result = 0
        else:
            result = int(lis[::-1])
            if result > (1<<31) - 1:
                result = 0
        return result