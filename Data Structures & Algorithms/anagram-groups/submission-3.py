from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for val in strs:
            count = [0] * 26
            for c in val:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            anagrams[key].append(val)

        return [ vals for vals in anagrams.values() ]