from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        max_count = 0
        for num in nums:
            counts[num] += 1
            max_count = max(max_count, counts[num])

        buckets = [ [] for _ in range(max_count+1) ]

        for num, count in counts.items():
            buckets[count].append(num)

        result = []

        for i in range(max_count, 0, -1):
            for num in buckets[i]:
                if len(result) == k:
                    return result
                result.append(num)

        return result