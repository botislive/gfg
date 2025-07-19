class Solution:
    def maxSum(self, arr):
        # code here
        max_sum=0
        sum=0
        for i in range(len(arr)-1):
            sum=arr[i]+arr[i+1]
            max_sum=max(sum,max_sum)
            
        return max_sum
            
    
