class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        count = ""
        i=0
        while i < len(s):
            while s[i] != "#":
                count += s[i]
                i += 1
            i += 1
            strs.append(s[i:i + int(count)])
            i += int(count)
            count = ""
        return strs