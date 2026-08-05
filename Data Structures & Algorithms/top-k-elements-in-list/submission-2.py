# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         dupli = defaultdict(list)
#         for num in nums:
#             if num in dupli:
#                 dupli[num] += 1
#             else:
#                 dupli[num] = 0
        
#         arr = []

#         for key, value in dupli.items():
#             arr.append([key, value])

#         sortedArr = sorted(arr, key = lambda x: x[1], reverse = True)
#         result = []
#         for i in range(0, k):
#             result.append(sortedArr[i][0])

#         return result


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        freq = [[] for _ in range(len(nums)+1)]

        for key, values in count.items():
            freq[values].append(key)
        res = []

        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                if len(res) < k:
                    res.append(j)
                else:
                    return res

        return res



        