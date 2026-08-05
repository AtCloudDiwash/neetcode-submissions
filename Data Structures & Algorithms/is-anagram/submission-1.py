class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        arr = [0]*26
        print(arr)

        for c in s:
            arr[ord(c)-ord('a')] += 1
        for c in t:
            arr[ord(c)-ord('a')] -= 1

        for count in arr:
            if count != 0:
                return False
        
        return True
        