class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        if res == strs:
            return []
        for s in strs:
            res += str(len(s)) + ","
        res += "#"

        for s in strs:
            res += s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        size = []
        i = 0
        res = []
        while s[i] != "#":
            length = ""
            while s[i] != ",":
                length += s[i]
                i += 1
            size.append(length)
            i += 1
        i += 1

        for sz in size:
            res.append(s[i: i + int(sz)])
            i += int(sz)
        return res

