class Solution:
    def arrayNesting(self, nums):

        max_count = 0
        read_list = []
        for i in range(0,len(nums)):
            #print (i)

            value = nums[i]
            if value in read_list:
                continue

            read_list.append(nums[i])
            count = 1
            while True:
                #print ("value:", value)
                value = nums[value]

                if value in read_list:
                    if count > max_count:
                        max_count = count
                    break

                else:
                    read_list.append(value)
                count+=1

        return max_count


class Solution1:
    def arrayNesting(self, nums):

        visited = [False] * len(nums)
        ans = 0
        for i in range(len(nums)):
            road = 0
            while not visited[i]:
                road += 1
                # 下面两行的顺序不能变
                visited[i] = True
                i = nums[i]
            ans = max(ans, road)
        return ans

if __name__ == '__main__':
    print (Solution().arrayNesting([5,4,0,3,1,6,2]))
