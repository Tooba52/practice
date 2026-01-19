class Solution:
    def isHappy(self, n: int) -> bool:
        total = n
        seen = []
        while total not in seen:
            seen.append(total)
            nums = str(total)
            nums = [int(c)**2 for c in nums]
            total = sum(nums)

        if total == 1:
            return True
        else:
            return False
            
        

if __name__=="__main__":
    sol = Solution()
    print(sol.isHappy(19))