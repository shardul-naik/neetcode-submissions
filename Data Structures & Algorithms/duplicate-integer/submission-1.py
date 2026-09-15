class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = set()
        for x in nums:
            if x in temp:
                return True
            temp.add(x)
        return False
