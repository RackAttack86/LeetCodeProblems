from typing import List

def twoSum(nums: List[int], target:int) -> List[int]:
    dict = {}
    for i in range(len(nums)):
        val = target - nums[i]
        if val in dict:
            return [dict[val], i]
        dict[nums[i]] = i
    return [] 
    
print(twoSum(nums=[2,7,11,15], target=9))