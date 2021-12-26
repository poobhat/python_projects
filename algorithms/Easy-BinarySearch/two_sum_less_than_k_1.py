class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # nums.sort
        result = []
        for idx1, val1 in enumerate(nums):
            for idx2, val2 in enumerate(nums):
                if idx1 != idx2 and val1 <= val2 and val1+val2 < k:
                    result.append(val1+val2)
        set(result)
        return -1 if result == [] else max(result)

if __name__ == "__main__":
    nums = [358,898,450,732,672,672,256,542,320,573,423,543,591,280,399,923,920,254,135,952,115,536,143,896,411,722,815,635,353,486,127,146,974,495,229,21,733,918,314,670,671,537,533,716,140,599,758,777,185,549]
    k = 1800
    obj = Solution()
    print(obj.twoSumLessThanK(nums, k))