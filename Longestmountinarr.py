class Solution(object):
    def longestMountain(self, arr):
        longestHeight = 0
        currHeight = 0
        
     
        currIdx = 1
        while currIdx < len(arr) -1:
            isPeak = arr[currIdx] > arr[currIdx -1] and arr[currIdx] > arr[currIdx + 1]
            if not isPeak:
                currIdx += 1
                continue
            leftIdx = currIdx - 2
            rightIdx = currIdx + 2
            while leftIdx >= 0 and arr[leftIdx] < arr[leftIdx + 1]:
                leftIdx -= 1
                
            while rightIdx < len(arr) and arr[rightIdx] < arr[rightIdx - 1]:
                rightIdx += 1
            currHeight = rightIdx - leftIdx - 1 
            longestHeight = max(longestHeight, currHeight)
            
            currIdx =  rightIdx
        return longestHeight
