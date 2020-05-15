"""
Problem name: Two Sum II - Input array is sorted

Description: Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        print("")
        print("numbers:{}".format(numbers))
        print("target:{}".format(target))
        list_len = len(numbers)
        i = 0
        first_index = None
        second_index = None
        prev_num = None

        for num in numbers:
            j = i + 1

            # Stop the loop if num > target (note that this is sorted list)
            if num > target:
                break

            # Avoid checking the same number again (note that this is sorted list)
            if prev_num is not None and num == prev_num:
                # increase the first index
                i = i + 1
                continue

            # Loop through all numbers next to chosen number (num)
            # Stop the loop
            #   -- when loop reached end of the list or
            #   -- when numbers[j] is <= or >= target depending on if target is +ve or -ve number
            while j < list_len and \
                    (
                            (target > 0 and numbers[j] <= target) or
                            (target <= 0 and numbers[j] >= target)
                    ):

                if num + numbers[j] == target:
                    # index pair found
                    first_index = i
                    second_index = j
                    # break while loop
                    break

                # increase the second index
                j = j + 1

            if first_index is not None:
                # index pair found
                # break for loop
                break

            # increase the first index
            i = i + 1
            prev_num = num
        # -- End of for loop

        if first_index is not None:
            print("Matched Index Pair:[{},{}]".format(first_index, second_index))
            print("Matched Value Pair:[{},{}]".format(numbers[first_index], numbers[second_index]))
            print("Returned Index Pair:[{},{}]".format(first_index+1, second_index+2))
            return [first_index+1, second_index+1]
        else:
            return[]


if __name__ == "__main__":
    s1 = Solution()
    returned_list = s1.twoSum(numbers=[2, 7, 11, 15], target=9)
    print(returned_list)
