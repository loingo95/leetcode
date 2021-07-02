class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        sorted_nums = sorted(unique_nums)
        if len(sorted_nums) < 3:
            return sorted_nums[-1]
        return sorted_nums[-3]
        