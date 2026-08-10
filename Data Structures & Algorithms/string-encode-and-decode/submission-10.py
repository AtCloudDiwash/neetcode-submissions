class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        first, second = 0, 0
        res = []

        if s == "":
            return []

        while second < len(s) - 1 and first < len(s) - 1:
            length = ""
            while s[first] != "#":
                length += s[first]
                first += 1
            second = first + 1
            res.append(s[second: second + int(length)])
            first += int(length) + 1
        return res




