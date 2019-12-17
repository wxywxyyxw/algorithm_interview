class Solution:
    def numTrees(self, n: int) -> int:
        path = 0
        step0 = 0
        step1 = 1
        if n == 1:
            return 1

        for i in range(2,n+1):
            path = step0 + 2 *step1
            step0 = step1
            step1 = path

        return path




if __name__ == '__main__':
    ret = Solution().numTrees(3)
    print (ret)
