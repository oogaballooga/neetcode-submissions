class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        output = []
        i=0
        while i < len(s):
            count = ""
            while s[i] != "#":
                count += s[i]
                i += 1
            i += 1
            output.append(s[i:i+int(count)])
            i += int(count)
        return output