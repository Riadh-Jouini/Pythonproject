nums = [1, 2, 6, 8]
target = 14

def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        seconde_valeur = target - nums[i]

        if seconde_valeur in nums:
            print([i, nums.index(seconde_valeur)])

twoSum(nums, target)
