class Solution_1(object):
    """Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique_elements = set()
        for item in nums:
            if item in unique_elements:
                return True
            unique_elements.add(item)
        return False


class Solution_2(object):
    """Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array."""

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = [0 for i in range(len(nums) + 1)]
        for num in nums:
            x[num] += 1
        for i in range(len(x)):
            if not x[i]:
                return i


class Solution_3(object):
    """Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums."""

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = [0 for i in range(len(nums))]
        for num in nums:
            x[num - 1] += 1
        ans = []
        for i in range(len(x)):
            if not x[i]:
                ans.append(i + 1)
        return ans


class Solution_4(object):
    """
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    You must implement a solution with a linear runtime complexity and use only constant extra space.

    Example 1:
    Input: nums = [2,2,1]
    Output: 1

    Example 2:
    Input: nums = [4,1,2,1,2]
    Output: 4

    Example 3:
    Input: nums = [1]
    Output: 1
    """

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for item in nums:
            ans = item ^ ans
        return ans


class Solution_5(object):
    """
    You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n.
    You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from original.
    The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array,
    the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.
    Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.
    """

    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if m * n != len(original):
            return []
        ans = [[None for _ in range(n)] for _ in range(m)]
        idx = 0
        for row_id in range(m):
            for col_id in range(n):
                ans[row_id][col_id] = original[idx]
                idx += 1
        return ans
    
    
class Solution_6(object):
    """ 
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such 
    that each unique element appears only once. The relative order of the elements should be kept the same. 
    Then return the number of unique elements in nums.
    Consider the number of unique elements of nums to be k, to get accepted, you need 
    to do the following things:  
    Change the array nums such that the first k elements of
    nums contain the unique elements in the order they were present in nums initially. 
    The remaining elements of nums are not important as well as the size of nums.
    """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow_idx, fast_idx = 0 , 0
        for fast_idx in range(1, len(nums)):
            if nums[fast_idx] != nums[slow_idx]:
                nums[slow_idx+1] = nums[fast_idx]
                slow_idx += 1
        return slow_idx+1
    
class Solution_7(object):
    """
    Given an integer array nums and an integer val, remove all occurrences of val 
    in nums in-place. The order of the elements may be changed. 
    Then return the number of elements in nums which are not equal to val.
    """
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow_idx = 0
        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[slow_idx] = nums[idx]
                slow_idx += 1
        for idx in range(slow_idx, len(nums)):
            nums[idx] = "_"
        return nums
    
class Solution_8(object):
    """
    Given a sorted array of distinct integers and a target value, return the index if the 
    target is found. If not, return the index where it would be if it were inserted in order.
    You must write an algorithm with O(log n) runtime complexity. 
    """
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left_idx, right_idx = 0, len(nums)
        while right_idx - left_idx > 1:
            middle_idx = (right_idx + left_idx) // 2
            middle_item = nums[middle_idx]
            if middle_item == target:
                return middle_idx
            elif middle_item > target:
                right_idx = middle_idx
            else:
                left_idx = middle_idx
        return left_idx+1
    
class Solution_9(object):
    """ 
    You are given a large integer represented as an integer array digits, where each digits[i] 
    is the ith digit of the integer. The digits are ordered from most significant 
    to least significant in left-to-right order. The large integer does not contain any leading 0's.
    Increment the large integer by one and return the resulting array of digits.
    """
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
        

class Solution_10(object):
    """ 
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
    and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
    Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    The final sorted array should not be returned by the function, but instead be 
    stored inside the array nums1. To accommodate this, nums1 has a length of m + n, 
    where the first m elements denote the elements that should be merged, and the last 
    n elements are set to 0 and should be ignored. nums2 has a length of n.
    """
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        left_idx, right_idx = m-1, n-1
        temp_idx = n+m-1
        while right_idx >= 0:
            if nums1[left_idx] <= nums2[right_idx]:
                nums1[temp_idx] = nums2[right_idx]
                right_idx -= 1
            else:
                nums1[temp_idx] = nums1[left_idx]
                left_idx -= 1
            temp_idx -= 1 
        return nums1

if __name__ == "__main__":
    # print(Solution_1().containsDuplicate([1, 2, 3, 2]))
    # print(Solution_2().missingNumber([3, 0, 1, 4, 2]))
    # print(Solution_3().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
    # print(Solution_3().findDisappearedNumbers([1, 1]))
    # print(Solution_4().singleNumber([1]))
    # print(Solution_5().construct2DArray(original=[1, 2, 3, 4, 5, 6], m=3, n=2))
    # print(Solution_5().construct2DArray(original=[1, 2, 3], m=1, n=3))
    # print(Solution_6().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    # print(Solution_7().removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))
    # print(Solution_8().searchInsert(nums = [1,3,5,6], target = 5))
    # print(Solution_9().plusOne(digits = [1, 3, 5, 9, 9]))
    # print(Solution_10().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
    print()
