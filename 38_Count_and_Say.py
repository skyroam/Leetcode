class Solution:
    def countAndSay(self, n: int) -> str:
        sequence = '1'  
        for j in range(n-1): 
            lis = []
            count = 0
            cha = sequence[0]
            #print("output",sequence)
            for i in range(len(sequence)):
                if sequence[i] == cha:
                    count += 1
                else:
                    lis.append(str(count))
                    lis.append(cha)
                    cha = sequence[i]
                    count = 1
                if i == len(sequence) -1:
                    lis.append(str(count))
                    lis.append(cha)
            sequence = lis
        return ''.join(sequence)