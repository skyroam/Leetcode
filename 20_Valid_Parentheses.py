class Solution:
    def isValid(self, s: str) -> bool:
        lis = list(s)
        stack = []
        while lis:
            cha = lis.pop(0)
            if cha in '([{':
                stack.append(cha)
            elif cha in ')]}':
                if (not stack) or ('([{'.index(stack[-1]) != ')]}'.index(cha)):
                    return False
                else:  
                    stack.pop()
        if stack: return False
        else: return True