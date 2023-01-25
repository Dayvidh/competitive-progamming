
class Solution: 
    def select(self, arr, i):
        # code here 
        return
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            doc = i
            for j in range(i, n):
                if arr[j] < arr[doc]:
                    doc = j
            arr[i], arr[doc] = arr[doc], arr[i]
        return arr    
