class Solution:
    def isPalindrome(self, x: int):
        nums = str(x)
        aslist = []
        for number in nums:
            aslist.append(number)
        aslist.reverse()
        if aslist == list(str(x)):
            return True
        else:
            return False

        

solution = Solution()
print(solution.isPalindrome(1221))
