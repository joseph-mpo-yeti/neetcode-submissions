class Solution:

    def encode(self, strs: List[str]) -> str:
        prefix = [str(len(strs))]
        for st in strs:
            prefix.append("_")
            prefix.append(str(len(st)))
            
        prefix.append(":")

        return "".join(prefix) + "".join(strs)

    def decode(self, s: str) -> List[str]:
        end_header = s.find(":")
        prefix = s[:end_header]
        print(prefix)
        lengths = [ int(val) for val in prefix.split("_") ]
        print(lengths)
        if lengths[0] == 0:
            return []
        else:
            strs = []
            final = s[end_header+1:]
            last_index = 0
            for i in range(1, len(lengths)):
                start = last_index
                last_index = end = start + lengths[i]
                strs.append(final[start:end])

            return strs
            