class Solution:
    def firstNegInt(self, arr, k): 
        i = 0
        j = 0
        lin = []
        out = []
        
        while j < len(arr):
            if arr[j] < 0:
                lin.append(arr[j])
            
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                if len(lin) == 0:
                    out.append(0)
                else:
                    out.append(lin[0]) 
                
                if lin and arr[i] == lin[0]:
                    lin.pop(0)

                i += 1
                j += 1

        return out

        
