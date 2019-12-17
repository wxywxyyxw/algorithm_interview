class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        count = len(num_str)
        max_dict = {}
        temp_max = int(num_str[-1])
        temp_max_index = count -1
        for index, item in enumerate(num_str[::-1]):
            if int(item) > temp_max:
                max_dict[count - index - 1] = (int(item),count - index - 1)
                temp_max = int(item)
                temp_max_index = count - index - 1
            else:
                max_dict[count - index - 1] = (int(temp_max),temp_max_index)
        print (max_dict)

        final_str = num_str
        for index,item in enumerate(num_str):
            max_num, max_index = max_dict[index]
            print (index,max_index,max_num)
            if int(item) < max_num:
                final_str = num_str[:index] + str(max_num) + num_str[index+1:max_index] + item + num_str[max_index+1:]
                break
        return final_str





if __name__ == '__main__':
    print (Solution().maximumSwap(2736))
