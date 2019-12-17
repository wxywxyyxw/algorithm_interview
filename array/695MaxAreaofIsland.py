class Solution:
    def maxAreaOfIsland(self, grid):

        row_count = len(grid)
        col_count = len(grid[0])

        read_list = []
        def _check_legal(i,j):
            if i >=0 \
                and i < row_count \
                and  j >=0 \
                and j < col_count \
                and (i,j) not in read_list \
                and a[i][j] == 1:
                return True
            return False

        max_num = 0
        for i in range(row_count):
            for j in range(col_count):
                if a[i][j] == 0:
                    continue

                if (i,j) in read_list:
                    continue

                queue = []
                n = 0
                queue.append((i,j))
                read_list.append((i,j))
                while queue:

                    i,j = queue.pop(0)
                    n+=1


                    if _check_legal(i,j+1):

                        queue.append((i,j+1))
                        read_list.append((i,j+1))

                    if _check_legal(i+1,j):
                        queue.append((i+1,j))
                        read_list.append((i+1,j))

                    if _check_legal(i-1,j):
                        queue.append((i-1,j))
                        read_list.append((i-1,j))

                    if _check_legal(i,j-1):
                        queue.append((i,j-1))
                        read_list.append((i,j-1))

                if n > max_num:
                    max_num = n

        return max_num













if  __name__ == '__main__':
    a = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print (Solution().maxAreaOfIsland(a))