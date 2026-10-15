class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Hashmap
        # Seen, if value in seen, return true, else f
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num);
        return False
