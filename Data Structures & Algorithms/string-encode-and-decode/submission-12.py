class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        res = ""

        for s in strs:
            res += str(len(s)) + ","
        res += "#"

        for s in strs:
            res += s
        print(res)
        return res



    def decode(self, s: str) -> List[str]:
        size = []
        l = 0
        res= []

        if s == "":
            return []

        while s[l] != "#":
            length = ""
            while s[l] != ",":
                length += s[l]
                l += 1
            size.append(int(length))
            l += 1
        l += 1

        for i in range(len(size)):
            res.append(s[l:l + size[i]])
            l += size[i]
        return res


                
        

