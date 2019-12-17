class Solution:
    def productExceptSelf(self, nums):
        count = len(nums)
        res = [1] * count

        for i in range(1,count):
            res[i] = nums[i-1] * res[i-1]
        print (res)
        item_value = nums[-1]
        for j in range(count-2,-1,-1):
            print (j)
            res[j] *= item_value
            item_value *=nums[j]
            print (res)
        return res







if __name__ == '__main__':
    print (Solution().productExceptSelf(
[9,0,-2]))

