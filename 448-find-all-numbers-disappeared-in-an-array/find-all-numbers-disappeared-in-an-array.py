class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_one=set(nums)
        lst=[] #empty list
        for i in range(1, len(nums)+1):
            if i not in set_one:
                lst.append(i)

        return lst
