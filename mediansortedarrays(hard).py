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
