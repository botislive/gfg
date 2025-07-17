#User function Template for python3
class Solution:
    def maximumSumSubarray (self,arr,k):
        i=0
        j=0
        maxs=-1
        sum=0
        while j<len(arr):
            sum+=arr[j]
            if j-i+1 <k:
                j+=1
            
            elif j-i+1==k:
                maxs=max(maxs,sum)
                sum-=arr[i]
                i+=1
                j+=1
            
        return maxs
       