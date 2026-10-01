class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we can do the brute force where we go through each one and determine if they add
        # we can instead check to see if a value has been seen of the difference
        # the difference allows us to find what we need at that index
        # use dict as we need a dictionary

        seen = {}
        for i in range(len(nums)):
            difference = target - nums[i] 

            if difference in seen:
                return [seen[difference],i]
            seen[nums[i]] = i


