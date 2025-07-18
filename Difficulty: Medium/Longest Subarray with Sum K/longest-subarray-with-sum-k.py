class Solution:
    def longestSubarray(self, arr, k):
        max_len = 0
        prefix_sum = 0
        seen = {}

        for i in range(len(arr)):
            prefix_sum += arr[i]

            # Case 1: If total sum from 0 to i is k
            if prefix_sum == k:
                max_len = i + 1

            # Case 2: If prefix_sum - k has been seen before
            if (prefix_sum - k) in seen:
                max_len = max(max_len, i - seen[prefix_sum - k])

            # Case 3: Only insert prefix_sum if not already in map
            if prefix_sum not in seen:
                seen[prefix_sum] = i

        return max_len

    
