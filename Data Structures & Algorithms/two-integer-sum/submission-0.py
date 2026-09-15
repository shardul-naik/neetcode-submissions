class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i in range(len(nums)):
            curr = nums[i]
            need = target - curr
            if need in temp:
                return [temp[need],i]
            temp[nums[i]] = i
