class Solution(object):

    def firstOcc(self, val, arr, lo, hi):
        mid = int((lo + hi) / 2)
        if lo > hi:
            return {"type": "insertionAt", "idx": lo}
        if arr[mid] == val:
            if mid - 1 > 0 and arr[mid - 1] == val: #not first occ
                return self.firstOcc(val, arr, lo, mid - 1) #search left half for 1st occ
            else:
                return {"type": "exact", "idx": mid} #return first occ
        elif arr[mid] < val:
            return self.firstOcc(val, arr, mid + 1, hi)
        else:
            return self.firstOcc(val, arr, lo, mid - 1)

    def lastOcc(self, val, arr, lo, hi):
        mid = int((lo + hi) / 2)
        if lo > hi:
            return {"type": "insertionAt", "idx": lo}
        if arr[mid] == val:
            if len(arr) > mid + 1 and arr[mid + 1] == val: #not last occ
                return self.lastOcc(val, arr, mid + 1, hi) #search right half for last occ
            else:
                return {"type": "exact", "idx": mid} #return first occ
        elif arr[mid] < val:
            return self.lastOcc(val, arr, mid + 1, hi)
        else:
            return self.lastOcc(val, arr, lo, mid - 1)

    def findMedianSub(self, nums1, nums2, lo, hi, num1Or2, k):
        if lo > hi:
            return None
        
        mid = int((lo + hi) / 2)
        arr = None
        arrOther = None
        
        if num1Or2 == 1:
            arr = nums1
            arrOther = nums2
        else:
            arr = nums2
            arrOther = nums1

        first = self.firstOcc(arr[mid], arrOther, 0, len(arrOther) - 1)
        last = first

        if first["type"] == "exact":
            last = self.lastOcc(arr[mid], arrOther, 0, len(arrOther) - 1)
            last["idx"] = last["idx"] + 1 #we have at least 2 numbers so could use the most left or most right (+1) one

        insertPointLo = first["idx"]
        insertPointHi = last["idx"]

        numLeftOfLo = mid + insertPointLo
        numLeftOfHi = mid + insertPointHi

        #print(k, mid, insertPointLo, insertPointHi)

        if k >= numLeftOfLo and k <= numLeftOfHi:
            return float(arr[mid])
        elif numLeftOfLo < k:
            return self.findMedianSub(nums1, nums2, mid + 1, hi, num1Or2, k)
        else:
            return self.findMedianSub(nums1, nums2, lo, mid - 1, num1Or2, k)

    def findMedianSortedArrays(self, nums1, nums2):
        total = len(nums1) + len(nums2)
        k = int(total / 2)
       
        if total % 2 == 1: #odd
            med = self.findMedianSub(nums1, nums2, 0, len(nums1) - 1, 1, k)
            if med == None:
                med = self.findMedianSub(nums1, nums2, 0, len(nums2) - 1, 2, k)
            return med
        else: #even
            hiMed = self.findMedianSub(nums1, nums2, 0, len(nums1) - 1, 1, k)
            if hiMed == None:
                hiMed = self.findMedianSub(nums1, nums2, 0, len(nums2) - 1, 2, k)
            
            loMed = self.findMedianSub(nums1, nums2, 0, len(nums1) - 1, 1, k - 1)
            if loMed == None:
                loMed = self.findMedianSub(nums1, nums2, 0, len(nums2) - 1, 2, k - 1)

            #print("lo: ", loMed, "hi: ", hiMed)
            return (loMed + hiMed) / 2


sol = Solution()
print(sol.findMedianSortedArrays([1,2], [1,2]))
print(sol.findMedianSortedArrays([1], [1]))
print(sol.findMedianSortedArrays([1,1], [1,1]))
print(sol.findMedianSortedArrays([1,2], [1,1]))
print(sol.findMedianSortedArrays([1,3], [2]))
print(sol.findMedianSortedArrays([1,2], [3,4]))
print(sol.findMedianSortedArrays([1], [2]))
print(sol.findMedianSortedArrays([1,3,5,6,7,999], [2,4,7,7,8]))
print(sol.findMedianSortedArrays([5,6,10,12,16,16,16,16], [3,4,5,6,8,8,8,9,11,17,21,22]))











