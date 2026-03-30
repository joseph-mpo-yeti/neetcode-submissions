class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        buckets = [set() for i in range(len(nums)+1)]
        
        for num, count in counts.items():
            buckets[count].add(num)

        print(buckets)

        result = []
        for i in range(len(nums), 0, -1):
            if len(result)>=k:
                break
            for val in buckets[i]:
                result.append(val)

            print(f"{result=}, {buckets=}")

        
        return result[:k]
            

        