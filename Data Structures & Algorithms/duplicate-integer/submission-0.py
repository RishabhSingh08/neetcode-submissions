class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Hashmap
        # Seen, if value in seen, return true, else f
        seen = {}
        for i, num in enumerate(nums):
            if seen.get(num, 0) == 1:
                return True
            else:
                seen[num] = seen.get(num, 0) + 1;
        return False
