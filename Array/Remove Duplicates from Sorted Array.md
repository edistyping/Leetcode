# Remove Duplicates from Sorted Array

## You are given an integer array prices where prices[i] is the price of a given stock on the ith day. On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day. Find and return the maximum profit you can achieve.

### TEST

```python
"""
    # Examples 
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

    Key Ideas:
        0. If length is 1 or first two are same, return only first value 
        1. set L (0) and R (1)
        2. Compare L and R, 
            If same, keep L and increment R
            If different, L = R then increment R and L to same position  

    Technique: 
        Array
        Two-pointer array

    Complexity:
        Time: O(n) for the single full traversal
        Space: O(1) for the variable 'l' we created  

"""
class Solution(object):
    def removeDuplicates(self, nums):
        
        if len(nums) <= 1:
            return 1
        elif len(nums) == 2 and nums[0] == nums[1]:
            return 1
        
        l = 0
        for r, num in enumerate(nums):
            if r == 1:
                pass

            if nums[l] != nums[r]:
                nums[l + 1] = nums[r]
                l += 1

        return l + 1
```

        