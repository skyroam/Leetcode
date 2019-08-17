class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, a in enumerate(nums):
            dif = target - a
            for j, b in enumerate(nums[i+1:]):
                if dif == b:
                    return [i, i+1+j]