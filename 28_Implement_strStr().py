class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        len1 = len(haystack)
        len2 = len(needle)
        if len1 < len2:
            return -1
        for i in range(len1):
            #print("i:",i)
            k = i
            if haystack[i] == needle[0] and (k+len2-1) < len1:
                for j in range(len2):
                    #print("k",k)
                    #print("j",j)
                    if haystack[k] != needle[j]:
                        break
                    k += 1
                else:
                    return i
        return -1