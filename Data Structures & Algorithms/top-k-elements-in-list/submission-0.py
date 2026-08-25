class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {value: frequency}
        count_map = {}
        for i in range(len(nums)):
            if nums[i] not in count_map:
                count_map[nums[i]] = 1
            else:
                count_map[nums[i]] += 1
        
        res = []
        while k:
            most_freq = max(count_map, key=count_map.get)
            res.append(most_freq)
            count_map.pop(most_freq)
            k -= 1
        return res

        