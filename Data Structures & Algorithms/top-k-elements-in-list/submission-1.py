class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dupli = defaultdict(list)
        for num in nums:
            if num in dupli:
                dupli[num] += 1
            else:
                dupli[num] = 0
        
        arr = []

        for key, value in dupli.items():
            arr.append([key, value])

        sortedArr = sorted(arr, key = lambda x: x[1], reverse = True)
        result = []
        for i in range(0, k):
            result.append(sortedArr[i][0])

        return result


        