#User function Template for python3

class Solution:
    
    # Function to return a list containing the union of the two arrays.
    def findUnion(self, a, b):
        return sorted(set(a + b))
