class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        existing = set(nums)

        for e in nums:
            # Determine if e is starting a sequence
            seq_length = 1

            if e - 1 not in existing:
                while e + seq_length in existing:
                    seq_length += 1


            if seq_length > longest:
                longest = seq_length
        
        return longest