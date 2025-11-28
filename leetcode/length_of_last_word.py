class Solution:
    def lengthOfLastWord(self, s: str):
        words = s.strip()
        words = words.split(" ")
        length = len(words[-1])
        return length


solution = Solution()
solution.lengthOfLastWord("  hello world  ")