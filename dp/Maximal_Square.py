class Solution:
    def maximalSquare(self, matrix) -> int:

        if not matrix:
            return 0

        if len(matrix[0]) == 1:
            return matrix[0][0]

        points = []
        read_points  = []
        count_row  = len(matrix)
        count_column = len(matrix[0])
        print (count_row,count_column)
        has_one = False

        if count_row < 2 or count_column < 2:
            for single_list in matrix:
                for item in single_list:
                    if item == "1":
                        return 1
            return 0

        for i in range(count_row-1):
            for j in range(count_column-1):
                print (i,j)
                if matrix[i][j] == "1" \
                    and matrix[i][j+1] == "1" \
                    and matrix[i+1][j] == "1" \
                    and matrix[i+1][j+1] == "1":

                    points.extend([(i,j),(i+1,j+1)])

                if matrix[i][j] == "1" \
                    or matrix[i][j+1] == "1" \
                    or matrix[i+1][j] == "1" \
                    or matrix[i+1][j+1] == "1":
                    has_one = True

        print (points,has_one)
        if not has_one:
            return 0
        if not points and has_one:
            return 1
        print (points)
        max = 0
        for item in points:
            if item in read_points:
                continue
            k=1
            i=1
            while True:


                if (item[0]+i,item[1]+i) in points:
                    read_points.append((item[0]+i,item[1]+i))
                    k+=1
                else:
                    if k > max:
                        max = k
                    break

                i+=1

        return max * max




if __name__ == '__main__':
    ret = Solution().maximalSquare([["0","1"]])
    print (ret)
