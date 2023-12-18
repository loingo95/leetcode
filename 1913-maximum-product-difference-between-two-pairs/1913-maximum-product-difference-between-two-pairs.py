class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        min_1, min_2 = nums[:2]
        max_1, max_2 = nums[-2:]
        return (max_1 * max_2) - (min_1 * min_2)