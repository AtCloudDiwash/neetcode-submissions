class Solution:

    def encode(self, strs: List[str]) -> str:

        en_str = ""
        for item in strs:
            en_str += str(len(item)) + "#" + item
        print(en_str)
        return en_str

    def decode(self, s: str) -> List[str]:
        dc_ls = []
        i = 0

        while i < len(s):
            j = i
            length = ""
            while s[j] != "#":
                length += s[j]
                j += 1
            
            dc_ls.append(s[j + 1: j + 1 + int(length)])
            i = j + 1 + int(length)
        return dc_ls
