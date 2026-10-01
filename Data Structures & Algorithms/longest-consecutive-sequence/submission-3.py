class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        existing = set(nums)

        for e in nums:
            # Determine if e is starting a sequence
            seq_length = 1
            dif = 1
            if e - 1 not in existing:
                while e + dif in existing:
                    dif += 1
                seq_length = dif

            if seq_length > longest:
                longest = seq_length
        
        return longest