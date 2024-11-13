class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_len = len(nums)
        permutations = []
        
        def backtrack_permute(permutation):
            if len(permutation) == nums_len:
                permutations.append(list(permutation))
                return
        
            # Traverse all list, but have to mind out already added number
            for num in nums:
                # using the distict property of 'nums' we can check if number is added correctly
                if num not in permutation:
                    permutation.append(num)
                    backtrack_permute(permutation)
                    permutation.pop()
                
        backtrack_permute([])
        return permutations