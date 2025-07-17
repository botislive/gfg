class Solution:
    def getSecondLargest(self, arr):
        maxi=-1
        smax=-1
        for i in range(len(arr)):
            if arr[i]>maxi:
                smax=maxi
                maxi=arr[i]
            elif arr[i]>smax and arr[i] !=maxi:
                smax=arr[i]
        return smax
        