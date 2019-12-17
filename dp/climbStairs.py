class Solution:
    def climbStairs1(self, n: int) -> int:

        def paths(n):
            if n==1 or n==0:
                return 1
            else:
                return paths(n-1) + paths(n-2)

        return paths(n)
    def climbStairs(self, n: int) -> int:
        path = 0
        step0 = 0
        step1 = 1
        for i in range(1,n+1):
            path = step0 + step1
            step0 = step1
            step1 = path

        return path


if __name__ == '__main__':
    ret = Solution().climbStairs(2)
    print (ret)
