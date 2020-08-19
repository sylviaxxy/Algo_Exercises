# LC 724 Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1

# LC 611 Valid Triangle Number
def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        while nums[0] == 0:
            nums.pop(0)
            if len(nums) < 3:
                return 0
        res = 0
        for i in range(len(nums)-2):
            k = i+2
            for j in range(i+1,len(nums)-1):
                while k < len(nums) and nums[k] < nums[i] + nums[j] :
                    k += 1
                res += k - j - 1
        return res

# 1282. Group the People Given the Group Size They Belong To
def regroup(size, G):
    ret = []
    while G:
        group_by_size = [G.pop(0) for i in range(size)]
        yield group_by_size

class Solution(object):
    def groupThePeople(self, groupSizes):
        dict = defaultdict(list)
        for i, g in enumerate(groupSizes):
            dict[g] += [i]
        ret = []
        for d in dict:
            ret += regroup(d, dict[d])
        return ret

# 1282. Group the People Given the Group Size They Belong To
# Solution 2
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        # store in dict by group sizes
        my_dict = defaultdict(list)
        for i in range(len(groupSizes)):
            my_dict[groupSizes[i]].append(i)
            
        # get right amount of IDs into each group
        res = []
        for key, key_list in my_dict.items():
            for i in range(0,len(key_list),key):
                res.append(key_list[i:i+key])
                
        return res
