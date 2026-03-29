from collections import deque

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        indices = set(nums)
        max_count = 0
        seen = set()
        
        for num in nums:
            if num in seen or num-1 in indices:
                continue

            val = num+1
            count = 1
            while val in indices and not val in seen:
                count += 1
                seen.add(val)
                val += 1

            seen.add(num)

            max_count = max(max_count, count)

        return max_count