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


if __name__ == "__main__":
    # print(Solution_1().containsDuplicate([1, 2, 3, 2]))
    # print(Solution_2().missingNumber([3, 0, 1, 4, 2]))
    # print(Solution_3().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
    # print(Solution_3().findDisappearedNumbers([1, 1]))
    # print(Solution_4().singleNumber([1]))
    # print(Solution_5().construct2DArray(original=[1, 2, 3, 4, 5, 6], m=3, n=2))
    # print(Solution_5().construct2DArray(original=[1, 2, 3], m=1, n=3))
