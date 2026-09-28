class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_freq = max(freq.values())

        ans = 0
        for count in freq.values():
            if count == max_freq:
                ans += count

        return ans

        
        