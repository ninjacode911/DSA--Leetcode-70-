class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)  # Step 1: Sort the array
        hashmap = {}  # Step 2: Store first occurrence index of each number
        
        for i, num in enumerate(sorted_nums):
            if num not in hashmap:  # Only store the first occurrence
                hashmap[num] = i

        return [hashmap[num] for num in nums]