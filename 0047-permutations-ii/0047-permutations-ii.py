class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # since nums is unique but index is not, so if we permute the indexes.
        # And then convert indexes to num then this is the same as permutation 1 problem.
        # It mean istead of do nums, we do list(range(len(nums))), in final step do converting back to nums
        # => This will not generating unique permutations, doing a final check to filter out wold do
        # But I don't think it's mean to be for this problem

#         # First submitsion
#         permutations = []
#         nums_len = len(nums)
#         nums_indexes = range(nums_len)
        
#         # sort first for easily check duplicate
#         # nums.sort()
        
#         def backtracking(permutation):
#             if len(permutation) == nums_len:
#                 nums_permutation = [nums[i] for i in permutation]
#                 if nums_permutation not in permutations:
#                     permutations.append(nums_permutation)
#                 return
                
#             for idx in nums_indexes:
#                 # nums now contain duplicated,
#                 # we can not simple check if num in permutation anymore
#                 # how about pop out the num so that it could not be add another time
#                 if idx not in permutation:
#                     permutation.append(idx)
#                     backtracking(permutation)
#                     permutation.pop()
                    
#         backtracking([])

        from collections import Counter
    
        permutations = []
        counter = Counter(nums)
        
        def backtracking(permutation):
            if len(permutation) == len(nums):
                permutations.append(list(permutation))
                return
            
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    backtracking(permutation + [num])
                    counter[num] += 1
                
        backtracking([])
        
        return permutations