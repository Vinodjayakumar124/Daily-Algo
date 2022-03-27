class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Given an List of numbers, find the index position of the target number,
        or returns the empty index if it is not present

        Args:
            nums: List of integers, sorted in ascending order
            target: Integer, represents required number
        
        Returns:
            Integer representing the index that target number is at, returns -1 if target is not found

        """
        start = 0 # front of list
        end = len(nums) - 1 # end of list 
        mid = (start + end) // 2 # middle of list
        
        # Check if target is at the end or front of list
        # reduces computational time w/o having to go through for loop
        if target == nums[-1]:
            return end
        elif target == nums[0]:
            return start
        
        #if start index and end index haven't overlapped, continue checking for the midpoint
        while start <= end:
            num = nums[mid]
            # if middle number is the target
            if num == target:
                return mid
            # if the middle number is less that target, target number is between middle and end
            elif num < target:
                start = mid + 1
            # if the middle number is greater than target, target number is between start and middle
            elif num > target:
                end = mid
            # reset the middle after re-assigning the start and end
            mid = (start + end) // 2
            # case where there is an overlap, returns -1
            if start >= end:
                return -1
        return mid