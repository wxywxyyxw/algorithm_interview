class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:

        if  obstacleGrid[0][0] == 1:
            return 0

        for i in range(len(obstacleGrid)):

            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1

        for i in range(len(obstacleGrid)):

            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == -1:
                    continue

                if i == 0 and j ==0:
                    obstacleGrid[i][j] = 1
                elif i - 1 < 0:
                    if obstacleGrid[i][j - 1] == -1:
                        obstacleGrid[i][j] = -1
                    else:
                        obstacleGrid[i][j] = max(0 + obstacleGrid[i][j - 1], 1)
                elif j -1 < 0:
                    if obstacleGrid[i - 1][j] == -1:
                        obstacleGrid[i][j] = -1
                    else:
                        obstacleGrid[i][j] = max(obstacleGrid[i - 1][j] + 0, 1)
                else:
                    if obstacleGrid[i - 1][j] == -1 and obstacleGrid[i][j - 1] == -1:
                        obstacleGrid[i][j] = -1
                    else:

                        one = obstacleGrid[i - 1][j] if obstacleGrid[i - 1][j] != -1 else 0
                        two = obstacleGrid[i][j - 1] if obstacleGrid[i][j - 1]!= -1 else 0
                        obstacleGrid[i][j] = max(
                            one
                            +
                            two
                            , 1)
                    #print (i,j,obstacleGrid[i][j],one,two)

        #print (obstacleGrid)
        if obstacleGrid[-1][-1] == -1:
            return 0
        else:
            return obstacleGrid[-1][-1]



if __name__ == '__main__':
    ret = Solution().uniquePathsWithObstacles([
        [0, 1, 0, 0, 0, 0],
        [1, 0,0,0,0],
        [0, 0,0,0,0],
        [0, 0,0,0,0]
    ])
    print(ret)
