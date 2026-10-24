class Solution:
    def isPalindrome(self, s: str) -> bool:

        word = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        l = 0
        r = len(word)-1

        if l == r:
            return True

        while l <= r:
            if word[l] == word[r]:
                l += 1
                r -= 1
            else:
                return False

        return True