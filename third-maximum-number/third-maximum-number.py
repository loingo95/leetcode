class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ## Naive
        # unique_nums = list(set(nums))
        # sorted_nums = sorted(unique_nums)
        # if len(sorted_nums) < 3:
        #     return sorted_nums[-1]
        # return sorted_nums[-3]

        unique_nums = list(set(nums))

        if len(unique_nums) < 3:
            return max(unique_nums)

        first = second = third = min(unique_nums)
        for num in unique_nums:
            if num >= first:
                third = second
                second = first
                first = num
            elif num >= second:
                third = second
                second = num
            elif num > third:
                third = num
        print(first, second, third)
        return third