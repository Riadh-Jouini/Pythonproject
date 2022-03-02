#Input: nums1 = [1,3], nums2 = [2]
#Output: 2.00000
#Explanation: merged array = [1,2,3] and median is 2.
#Example 2:

#Input: nums1 = [1,2], nums2 = [3,4]
#Output: 2.50000
#Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

#Constraints:

#nums1.length == m
#nums2.length == n
#0 <= m <= 1000
#0 <= n <= 1000
#1 <= m + n <= 2000
#-106 <= nums1[i], nums2[i] <= 106

from __future__ import division
import math

nums1 = [1,3]
nums2 = [2,4]
nums3 = nums1+nums2
sorted_nums = sorted(nums3)
def split_list(sorted_nums):
    half = len(sorted_nums)//2
    return sorted_nums[:half], sorted_nums[half:]

def function():
    B, C  = split_list(sorted_nums)
    D = float(B[-1]+C[0])//2
    if len(sorted_nums) % 2 == 0:
        print(float(D))
    elif len(sorted_nums) % 2 != 0:
        print(C[0])
    print((B[-1]+C[0])/2)
function()
