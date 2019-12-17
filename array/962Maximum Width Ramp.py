class Solution:
    def maxWidthRamp(self, A) -> int:
        stack = [(0,A[0])]
        max_len = 0
        for i, item in enumerate(A):
            if stack and stack[-1][1] > item:
                stack.append((i,item))
            else:
                #print ("stack {} i {} item {}".format(stack,i,item))
                for j,tu in enumerate(stack):
                    if tu[1] <= item:
                        max_len = max(i-tu[0], max_len)
                        #print ("break")
                        break

            #print (max_len)
        #print (stack)

        return max_len

    def maxWidthRamp2(self, A) -> int:
        stack = [(0,A[0])]
        max_len = 0
        for i, item in enumerate(A):
            if stack and stack[-1][1] > item:
                stack.append((i,item))

                for
        #     else:
        #         #print ("stack {} i {} item {}".format(stack,i,item))
        #         for j,tu in enumerate(stack):
        #             if tu[1] <= item:
        #                 max_len = max(i-tu[0], max_len)
        #                 #print ("break")
        #                 break
        #
        #     #print (max_len)
        # #print (stack)

        return max_len




if __name__ == '__main__':
    print (Solution().maxWidthRamp(
[3,4,1,2]))
