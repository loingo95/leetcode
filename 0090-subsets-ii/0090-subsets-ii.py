class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        power_set = []
        nums.sort()

        def back_track_subset(current_idx, subset):
            power_set.append(list(subset))

            for idx in range(current_idx, len(nums)):
                # prevent dupicate adding num, the previous num is already added 
                # current num so skip the duplicated 
                if idx != current_idx and nums[idx] == nums[idx-1]:
                    continue
                subset.append(nums[idx])
                back_track_subset(idx+1, subset)
                subset.pop()

        back_track_subset(0, [])

        return power_set