class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # count frequency

        collect_maps = {}

        for n in nums:
            if n in collect_maps:
                collect_maps[n] += 1
            else:
                collect_maps[n] = 1

        # make a sorted map based on the values of the map
        sorted_map = sorted(collect_maps, key = collect_maps.get, reverse = True)
        final_map = []
        print(sorted_map)

        # append top k keys from the final_map array and return the array

        for i in range(0, k):
            final_map.append(sorted_map[i])
        
        return final_map
            
