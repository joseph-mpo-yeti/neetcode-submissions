class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_cnt = 0

        for num in num_set:
            if num-1 in num_set:
                continue
            
            cnt = 1
            val = num+1
            while val in num_set:
                cnt += 1
                val += 1
            
            max_cnt = max(max_cnt, cnt)

        return max_cnt