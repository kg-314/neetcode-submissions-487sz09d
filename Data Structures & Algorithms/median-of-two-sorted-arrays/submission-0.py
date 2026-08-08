class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)

        p1 = 0
        p2 = 0

        newArr = []

        for i in range(0, length):

            if p1 >= len(nums1):
                newArr.append(nums2[p2])
                p2 += 1
            elif p2 >= len(nums2):
                newArr.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                newArr.append(nums1[p1])
                p1 += 1
            else:
                newArr.append(nums2[p2])
                p2 += 1
        
        if len(newArr) != 0:
            if len(newArr) % 2 == 0:
                m = (len(newArr) - 1) // 2
                return (newArr[m] + newArr[m + 1]) / 2
            else:
                m = len(newArr) // 2
                return newArr[m]
        return 0