class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge_sort_top_down(nums):
            if len(nums) <=1:
                return nums
            
            pivot = len(nums) // 2
            left = merge_sort(nums[:pivot])
            right = merge_sort(nums[pivot:])
            
            return merge(left, right)
        
        def merge_sort_bottom_up(nums):
            if len(nums) <=1:
                return nums
            
            sorted_list = [[num] for num in nums]
            
            while(len(sorted_list) > 1):
                merged_list = []
                idx = 0
                while idx < len(sorted_list):
                    if idx < len(sorted_list) - 1:
                        merged_list.append(merge(sorted_list[idx], sorted_list[idx+1]))
                        idx += 2
                    elif idx == len(sorted_list) - 1:
                        merged_list.append(sorted_list[idx])
                        break
                        
                        
                sorted_list = merged_list
                
                
            return sorted_list[0]
        
        
        
        def merge(l1, l2):
            l1_pointer = l2_pointer = 0
            sorted_list = []
            while (l1_pointer < len(l1)) and (l2_pointer < len(l2)):
                if l1[l1_pointer] < l2[l2_pointer]:
                    sorted_list.append(l1[l1_pointer])
                    l1_pointer += 1
                    
                else:
                    sorted_list.append(l2[l2_pointer])
                    l2_pointer += 1
                    
                    
            sorted_list.extend(l1[l1_pointer:])
            sorted_list.extend(l2[l2_pointer:])
                
            return sorted_list
        
        
        return merge_sort_bottom_up(nums)
            
            