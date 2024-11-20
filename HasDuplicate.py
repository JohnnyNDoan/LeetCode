'''
    Time = O(n) Space = O(n)
    Use of hashset to check duplicates in a set
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                retrun True
            hashset.add(n)
        return False