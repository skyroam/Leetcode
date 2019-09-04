class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = None
        j = -1   #label the index of item
        for i in range(len(nums)):
            j += 1
            if temp == nums[j]:
                nums.pop(j)
                j -= 1
            else:
                temp = nums[j]
        return len(nums)