class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_str = bin(n)[2:]
        return bin_str.count('1')