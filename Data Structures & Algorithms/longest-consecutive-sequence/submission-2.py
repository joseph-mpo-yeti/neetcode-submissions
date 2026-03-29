from collections import deque

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        indices = { nums[i]: i for i in range(len(nums)) }
        max_count = 0
        seen = set()
        
        for num in nums:
            if num in seen:
                continue
            
            val = num-1
            count = 1
            while val in indices:
                count += 1
                seen.add(val)
                val -= 1

            val = num+1
            while val in indices:
                count += 1
                seen.add(val)
                val += 1

            seen.add(num)

            max_count = max(max_count, count)

        return max_count