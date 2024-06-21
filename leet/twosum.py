class Solution(object): #define the class for an object
    def twoSum(self, nums, target): #define class method, the name of the problem
        for idx, val in enumerate(nums): #find the index and its value for each element in nums (iteration)
            '''
            if the difference between the target and the current value
            is in the remaining indices after the current value's index (+1 because inclusive)
            '''
            if (target - val) in nums[(idx + 1):]:
                '''
                return the first index
                and then return the index of the target value within the remaining elements
                finally, add the skipped over elements (+ idx + 1)
                '''
                return idx, nums[(idx + 1):].index(target-val) + idx + 1
                

answer = Solution() #instance creation

print(answer.twoSum(nums=[2, 7, 11, 15], target=9)) #test case 1

print(answer.twoSum(nums=[3, 2, 4], target=6)) #test case 2

print(answer.twoSum(nums=[3, 3], target=6)) #test case 3