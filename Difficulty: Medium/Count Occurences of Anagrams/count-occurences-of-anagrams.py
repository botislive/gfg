from collections import Counter

# User function Template for python3
class Solution:
    def search(self, pat, txt):
        k = len(pat)
        n = len(txt)
        i = 0
        j = 0
        count = 0
        window = ""
        
        pat_count = Counter(pat)
        window_count = Counter()
        
        while j < n:
            window_count[txt[j]] += 1

            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                if window_count == pat_count:
                    count += 1

                window_count[txt[i]] -= 1
                if window_count[txt[i]] == 0:
                    del window_count[txt[i]]

                i += 1
                j += 1

        return count
