class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash_map_with_value_as_idx = {num:idx for idx,num in enumerate(nums)}
        for num_idx, num in enumerate(nums):
            difference = target - num
            # check if difference in hashed map, and it's not the same index, mean num+num
            if (
                difference in nums_hash_map_with_value_as_idx
                and nums_hash_map_with_value_as_idx[difference] != num_idx
            ):
                return [num_idx, nums_hash_map_with_value_as_idx[difference]]
        return []
