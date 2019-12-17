class Solution:
    # def numDecodings(self, s: str) -> int:
    #
    #     total = 0
    #
    #     def cal_count(last_sep,index):
    #         if last_sep + 1 == index:
    #             return 1
    #         else:
    #             return index - last_sep -1
    #
    #     str_list = s.split('0')
    #     count =0
    #     flag = False
    #     for x in str_list:
    #         if len(x)==1:
    #             count+=1
    #         elif len(x) > 1:
    #             flag = True
    #
    #     if count >1 or flag == True:
    #         total=1
    #
    #     for item in s.split('0'):
    #         last_sep = -1
    #         if item:
    #             for index in range(len(item)):
    #                 if index == len(item) -1:
    #                     if last_sep != index -1:
    #                         total += cal_count(last_sep,index)
    #                     else:
    #                         total +=1
    #
    #                 elif int(item[index]) * 10 + int(item[index+1]) > 26:
    #                     total += cal_count(last_sep,index)
    #                     last_sep = index
    #
    #     return total
    #
    def numDecodings_wrong(self, s: str) -> int:
        pass
    #     if '0' in s:
    #         return 0
    #     if len(s) == 1:
    #         return 1
    #
    #     total = 0
    #     last_sep = -1
    #
    #     def cal_count(last_sep,index):
    #         if last_sep + 1 == index:
    #             return 1
    #         else:
    #             return index - last_sep -1
    #
    #     for index in range(len(s)):
    #         if index == len(s) -1:
    #             if last_sep != index -1:
    #                 total += cal_count(last_sep,index)
    #             else:
    #                 total +=1
    #
    #         elif int(s[index]) * 10 + int(s[index+1]) > 26:
    #             total += cal_count(last_sep,index)
    #             last_sep = index
    #
    #     return total + 1

if __name__ == '__main__':
    ret = Solution().numDecodings('12')
    print (ret)
