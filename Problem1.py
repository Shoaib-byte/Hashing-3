class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return list()
        hmap = {}
        hmap['A'] = 1
        hmap['C'] = 2
        hmap['G'] = 3
        hmap['T'] = 4

        hset = set()
        result = set()
        currHash = 0
        for i in range(10):
            inn = s[i]
            currHash = currHash * 4 + hmap[inn]
        hset.add(currHash)
        for i in range(1,n - 9): 
            #outgoing char
            out = s[i-1]
            currHash = currHash - pow(4,9) * hmap[out]
            #incoming char
            inn = s[i+9]
            currHash = currHash * 4 + hmap[inn]

            if currHash in hset:
                result.add(s[i:i+10])
            else:
                hset.add(currHash)
        
        return list(result)


        