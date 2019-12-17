class Solution:
    def longestPalindrome1(self, s: str) -> str:
        first_index = 0
        last_index = 0
        longest = 1

        def find_sub(pre,nex,s,first_index,last_index,longest):

            while pre >=0 and nex < len(s):
                print (pre,nex)
                if s[pre] == s[nex]:
                    count = nex - pre + 1

                    if count > longest:
                        first_index = pre
                        last_index = nex
                        longest = count
                    pre = pre -1
                    nex = nex + 1
                else:
                    break

            return first_index, last_index, longest

        for i in range(0,len(s)-1):
            print ("i:",i)
            if i > 0:
                if s[i-1] == s[i+1]:
                    pre = i-1
                    nex = i+1
                    first_index, last_index, longest = find_sub(pre,nex,s,first_index,last_index,longest)

            if s[i] == s[i+1]:
                if longest < 2:
                    longest = 2
                    first_index = i
                    last_index = i+1
                pre = i-1
                nex = i+2

                first_index, last_index, longest = find_sub(pre,nex,s,first_index,last_index,longest)



        print (first_index,last_index)
        return s[first_index:last_index+1]
    def longestPalindrome(self, s: str) -> str:
        longest = -1
        first = 0
        last = 0

        while True:
            i = 0
            j = len(s)-1

            tuples = [(i,j),(i,j-1),(i+1,j)]
            for tuple in tuples:
                m,n = tuple
                if m >=n:
                    continue
                count = n - m + 1
                if count % 2 !=0:
                    if s[m:(m-n)/2+1] == s[((m-n)/2+2):n+1]:
                        if count > longest:
                            longest = count
                            first = m
                            last = n
                else:
                    pass





def stringToString(input):
    import json

    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line)

            ret = Solution().longestPalindrome(s)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    ret = Solution().longestPalindrome1("ccc")
    print (ret)