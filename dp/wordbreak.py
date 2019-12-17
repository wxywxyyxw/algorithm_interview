class Solution:
    def wordBreak(self, s, wordDict) -> bool:

        str_list = [0]
        while len(str_list) !=0:
            index = str_list[0]
            txt = s[index:]

            #print (txt)
            str_list = str_list[1:]
            for word in wordDict:
                try:
                    index_head = txt.index(word)
                except:
                    continue

                if index_head  == 0:
                    if len(word) == len(txt):
                        return True
                    else:
                        #print (len(word),-1)
                        str_list.append(index+len(word))

        return False

if __name__ == '__main__':
    ret = Solution().wordBreak(
        "leetcode",
        ["leet","code"]
    )
    print (ret)


