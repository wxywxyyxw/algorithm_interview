class Solution:
    def uniquePaths_too_slow(self, m: int, n: int) -> int:
        path_count = 0

        def find_path(m,n):
            #print (m,n)
            if m==1 or n==1:
                return 1
            return find_path(m-1,n) + find_path(m,n-1)

        return find_path(m,n)

    def uniquePaths_too_slow2(self, m: int, n: int) -> int:
        point_tuples = [(m,n)]
        paths = 0
        while len(point_tuples)!=0:
            x,y = point_tuples[0]
            point_tuples = point_tuples[1:]

            if x == 1 or y == 1:
                paths +=1
            else:
                point_tuples.extend([(x-1,y),(x,y-1)])

        return paths

    def uniquePaths_too_slow3(self, m: int, n: int) -> int:
        paths = 0

        def find_path(m,n):
            #print (m,n)


            # if m == 0 or n==0:
            #     #print ("break: ",m,n)
            #     return

            if m == 1 or n == 1:
                #print ("return: ",m,n)
                yield 1
            else:
                yield from find_path(m-1,n)

                yield from find_path(m,n-1)

        for i in find_path(m,n):
            paths +=i
        return paths

    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                dp[i][j] = max(dp[i - 1][j] + dp[i][j - 1], 1)
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    ret = Solution().uniquePaths(23,12)
    print (ret)
