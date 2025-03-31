class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={} #v=values, i=index
      
    
        for indx,val in enumerate(nums):
            diff=target-val
            if diff in hashmap:
                return [indx,hashmap[diff]]
            hashmap[val]=indx #we use this to put it in the hashmap so for any further look ups





