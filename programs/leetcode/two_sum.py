"""
Problem name: Two Sum

Description: Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print("")
        print("nums:{}".format(nums))
        print("target:{}".format(target))
        list_len = len(nums)
        i = 0
        first_index = None
        second_index = None

        for num in nums:
            j = i + 1
            while j < list_len:
                if num + nums[j] == target:
                    first_index = i
                    second_index = j
                    break
                j = j + 1

            i = i + 1

            if first_index is not None:
                break

        if first_index is not None:
            print("Matched Index Pair:[{},{}]".format(first_index, second_index))
            print("Matched Value Pair:[{},{}]".format(nums[first_index], nums[second_index]))
            print("Returned Index Pair:[{},{}]".format(first_index+1, second_index+2))
            return [first_index, second_index]
        else:
            return []


if __name__ == "__main__":
    s1 = Solution()
    returned_list = s1.twoSum(nums=[2, 7, 11, 15], target=9)
    print(returned_list)
