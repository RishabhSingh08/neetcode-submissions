class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash, value : index, compare target - i to hash[value]
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i