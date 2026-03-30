class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for val in strs:
            count = [0] * 26
            for c in val:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            if key in anagrams:
                anagrams[key].append(val)
            else:
                anagrams[key] = [val]

        return [ vals for vals in anagrams.values() ]