class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        if len(strs) == 1 and strs[0] == "":
            return ""
        for item in strs:
            final_str += str(len(item)) + item
        return final_str

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
            
        first = 0
        last = int(s[0])
        res = []
        while last <= len(s):
            res.append(s[first+1: last+1])
            first = last + 1
            last = last + last + 1

        return res

            

        
            

