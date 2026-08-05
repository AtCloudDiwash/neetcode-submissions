class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes = []
        res = ""

        for item in strs:
            sizes.append(str(len(item)))

        res = ",".join(sizes)
        res += ","
        res += "#"
        res += "".join(strs)
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes = []
        res = []
        counter = 0

        while s[counter] != "#":
            counterTwo = counter
            while s[counterTwo] != ",":
                counterTwo += 1
            sizes.append(int(s[counter:counterTwo]))
            counter = counterTwo + 1
        counter += 1
        for sz in sizes:
            res.append(s[counter: counter + sz])
            counter += sz
        print(res)
        return res
        


       
                
