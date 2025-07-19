class Solution:
    def leaders(self, arr):
        out = []
        maxi = float('-inf')  # Handle negative values too
        
        arr = arr[::-1]  # Reverse the array

        for i in range(len(arr)):
            if arr[i] >= maxi:
                out.append(arr[i])
                maxi = arr[i]  # Update the correct variable

        return out[::-1] 
