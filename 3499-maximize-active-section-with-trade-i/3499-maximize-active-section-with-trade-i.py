class Solution:

  def maxActiveSectionsAfterTrade(self, s: str) -> int:
    initial_ones = s.count('1')

    zero_blocks = [len(block) for block in s.split('1') if block]

    max_gain = 0
    for i in range(len(zero_blocks) - 1):
      max_gain = max(max_gain, zero_blocks[i] + zero_blocks[i + 1])

    return initial_ones + max_gain