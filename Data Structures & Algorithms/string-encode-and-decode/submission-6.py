class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        if strs == res:
            return []
        
        for s in strs:
            res += str(len(s)) + ","
        res += "#"
        for s in strs:
            res += s
  
        return res 

    def decode(self, s: str) -> List[str]:
        size = []
        i, j = 0, 0

        while s[i] != "#":
            length = ""
            while s[i] != ",":
                length += s[i]
                i += 1
            size.append(int(length))
            i += 1
        counter = 0
        res = []
        i += 1
        while counter < len(size):
            res.append(s[i: i + size[counter]])
            i += size[counter]
            counter += 1
        return res

    
