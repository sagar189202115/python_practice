nums1=[1,2]
nums2=[3,4]
newlist = (nums1 + nums2)
newlist.sort()
if (len(nums1) + len(nums2)) % 2 == 1:
    print(newlist[(len(newlist) - 1) // 2])
else:
    print(newlist)
    print((newlist[((len(newlist) - 1) // 2)] + (newlist[len(newlist) // 2])) / 2)