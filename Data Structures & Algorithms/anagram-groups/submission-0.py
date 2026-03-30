class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for val in strs:
            key = "".join(sorted(val))
            if key in anagrams:
                anagrams[key].append(val)
            else:
                anagrams[key] = [val]

        return [ vals for vals in anagrams.values() ]