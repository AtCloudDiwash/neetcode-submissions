class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = strs.copy()
        for i in range(0, len(strs)):
            temp[i] = "".join(sorted(strs[i]))
        dupli = {}
        for i in range(0, len(strs)):
            if temp[i] in dupli:
                dupli[temp[i]].append(i)
            else:
                dupli[temp[i]] = [i]
        res = []
        for key, value in dupli.items():
            arr = []
            while len(value) > 0:
                arr.append(strs[value.pop()])
            res.append(arr)
        return res

        



            
        