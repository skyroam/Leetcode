class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = -1
        for i in range(len(nums)):
            j += 1
            if nums[j] == val:
                nums.pop(j)
                j -= 1
        return len(nums)