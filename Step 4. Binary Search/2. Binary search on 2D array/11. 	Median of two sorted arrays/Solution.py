class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def median(arr1,arr2,x,y):
            if x>y:
                return median(arr2,arr1,y,x)
            low= 0
            high= x
            import sys
            while low<=high:
                cut1= (low+high)>>1
                cut2= int((x+y+1)/2)-cut1
                l1= ~sys.maxsize if cut1==0 else arr1[cut1-1]
                l2= ~sys.maxsize if cut2==0 else arr2[cut2-1]
                r1= sys.maxsize if cut1==x else arr1[cut1]
                r2= sys.maxsize if cut2==y else arr2[cut2]
                if l1<=r2 and l2<=r1:
                    if (x+y)%2==1:
                        return max(l1,l2)
                    else:
                        return (max(l1,l2)+min(r1,r2))/2.0
                elif l1>r2:
                    high= cut1-1
                else:
                    low= cut1+1
            return 0.0
        n= len(nums1)
        m= len(nums2)
        return median(nums1,nums2,n,m)
        
