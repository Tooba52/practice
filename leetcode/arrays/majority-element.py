class Solution:
    def majorityElement(self, nums: list):
        #TC = O(N^2), SC = O(N)
        # occurances = {}
        # for number in nums:
        #     occurances[number] = nums.count(number)
        # return max(occurances, key=occurances.get)

        #TC = O(N^2), SC = O(1)
        # current_occurance = 0
        # most_occurance = 0
        # most = 0
        # for number in nums:
        #     current_occurance = nums.count(number)
        #     if current_occurance > most_occurance:
        #         most_occurance = current_occurance
        #         most = number
        # return most

        #TC = O(N), SC = O(1)
        count = 0
        candidate = nums[0]

        for number in nums:
            if candidate == number:
                count+=1
            else:
                count-=1
                if count <= 0:
                    candidate = number
                    count=1
        return candidate
            


solution = Solution()
print(solution.majorityElement([3,2,3])) #3
print(solution.majorityElement([3,3,4])) #3
print(solution.majorityElement([2,2,1,1,1,2,2])) #2

#TC = O(N)
#SC = O(1)