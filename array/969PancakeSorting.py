class Solution:
    def pancakeSort(self, A):
        list_change = []
        b = sorted(A, reverse=True)
        count = len(A)
        for i in range(count):
            index = A.index(b[i])
            if index != count -i-1:
                print (index,b[i],A)
                A = A[:index+1][::-1] + A[index+1:]
                print (A)
                A = A[:count - i][::-1] + A[count - i:]
                print (A,'----------',index+1,count - i)

                if index !=0:
                    list_change.append(index+1)
                list_change.append(count - i)
        print ('---->',list_change)









        print(A)


if  __name__ == '__main__':
    a = [3,2,4,1]
    Solution().pancakeSort(a)
