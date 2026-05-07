"""
80. Remove Duplicates from Sorted Array II
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. 
You must do this by modifying the input array in-place with O(1) extra memory.
"""
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Given an integer array sorted in ascending order.

        Task : Remove duplicates in-place such that 
                each element appears at most twice.

        Note: Relative order of the elements should be kept the same.

        Example: 
        nums = [1, 1, 1, 2, 2, 3]

        Expected o/p : [1, 1, 2, 2, 3, _]

        Relative Order: 1 -> 2 -> 3
            "1 comes before 2 and 2 comes before 3 and 3 comes last."

        #  In-place-modification implies no such change in length
            Expected o/p : [1, 1, 2, 2, 3, _]
            One element is removed return len(nums) - 1 => 6 - 1 = 5
        """
        #  if the given array is empty return 0
        if not nums:
            return 0

        #  initialize variables
        #  keeps track of indices of elements in the array
        i = 1
        j = 1

        #  cnt keeps track of the number of times an element is present
        cnt = 1

        #  check the condition i is less than the actual length of nums
        while i < len(nums):
            #  check whether nums[i] equals to nums[i - 1]
            if nums[i] == nums[i - 1]:
                #  if they both are equal
                #  increment it's cnt by 1
                cnt += 1

                #  check if the count is greater than 2 or not
                if cnt > 2:
                    i += 1
                    continue

            #  if nums[i] is not equal to nums[i - 1]
            else: 
                #  initialize the cnt to 'zero'
                cnt = 1

            nums[j] = nums[i]
            #  increment the index pointer
            i += 1
            j += 1

        del nums[j:]

        #  finally, return the length of nums 
        #  as it implies the number of element appears atmost twice
        return len(nums)


s = Solution()
print(s.removeDuplicates([1,1,1,2,2,3]))

# problem: 80-remove-duplicates-from-sorted-array-II