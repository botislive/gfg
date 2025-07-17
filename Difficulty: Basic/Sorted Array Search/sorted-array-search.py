#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        for num in arr:
            if num==k:
                return True
        return False
        #Your code here