"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

def twoSum(arr, target):
    # Simple solution: Two for loops
    outputArr = []
    for i in range(len(arr)):
        numToFind = target - arr[i];
        for j in range(len(arr)):
            if(arr[j] == numToFind and j != i):
                outputArr.append(i)
                outputArr.append(j)
                return outputArr
    return []

if __name__ == '__main__':
    arr1 = [2,7,11,15]
    print(twoSum(arr1, 9)) # [0, 1]

    arr2 = [3,2,4]
    print(twoSum(arr2, 6)) # [1, 2]

    arr3 = [3,3]
    print(twoSum(arr3, 6)) # [0, 1]

    # Follow-up
    # TODO: Followup