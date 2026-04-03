class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0;
        stack = [];
        if not nums:
            return False;
        while i < len(nums):
            if nums[i] in stack:
                return True;
            stack.append(nums[i])
            i += 1;
        return False