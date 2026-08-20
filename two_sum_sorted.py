"""
Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in
non-decreasing order, find two numbers such that they add up to a specific
target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= len(numbers).

Return the indices of the two numbers, index1 and index2, added by one as an
integer array [index1, index2].

The tests are generated such that there is exactly one solution. You may not
use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2, 7, 11, 15], target = 9
Output: [?, ?]
Explanation: Find the two indices whose values add up to target.

Constraints:

- 2 <= len(numbers) <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order.
- -1000 <= target <= 1000
- The tests are generated such that there is exactly one solution.
"""


class Solution:
    def twoSum(self, numbers, target):
        
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            else:
                right -= 1
        return False

solve = Solution().twoSum([2, 7, 11, 15], 9)
print(solve)