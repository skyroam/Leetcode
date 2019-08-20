class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        num = len(strs)
        if num == 0:
            return ""
        elif num == 1:
            return strs[0]
        else:
            min_ = len(strs[0])
            index = 0
            for ind, item in enumerate(strs):
                if len(item) < min_:
                    min_ = len(item)
                    index = ind

            for i in range(min_):
                for j in range(num-1):
                    if strs[j][i] != strs[j+1][i]:
                        return strs[index][:i]
            return strs[index]