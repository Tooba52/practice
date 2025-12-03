class Solution:
    def twoSum(self, nums: list, target: int):
        numbers = {}
        pos = 0
        for number in nums:
            find = target - number
            if find in numbers:
                return sorted([pos,numbers[find]])
            else:
                numbers[number] = pos
            pos +=1        


solution = Solution()
print(solution.twoSum([2,7,11,15],9)) #0,1
print(solution.twoSum([3,2,4],6)) #1,2
print(solution.twoSum([3,3],6)) #0,1
print(solution.twoSum([5,3,5],10))