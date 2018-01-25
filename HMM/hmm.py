#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import math
import pickle

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

WORD_TYPES = 4  # 1:词开头 2:词中间 3:词结束 4:单个字成词，
WORD_HEAD = 0
WORD_MIDDLE = 1
WORD_END = 2
WORD_SINGLE = 3
WORD_MAX_ENCODE = 65536
INFINITE = float(-2 ** 31)


class DiscreteHMM(object):
    def __init__(self):
        # 隐状态个数
        self.pi_list = np.zeros(WORD_TYPES)
        # 状态转移矩阵
        self.a = np.zeros((WORD_TYPES, WORD_TYPES))
        # 观测概率矩阵
        self.b = np.zeros((WORD_TYPES, WORD_MAX_ENCODE))

    def train(self, file_path):
        with open(file_path) as f:
            data = f.read()[3:].decode('utf-8')  # 去掉BOM头
            words = data.split('  ')
            self._train(words)
            self._save()

            print ('train success')

    def segment(self, file_path):
        with open(file_path) as f:
            data = f.read()[3:].decode('utf-8')
            decode_list = self._viterbi(data)
            return self._create_segment(data,decode_list)

    def _viterbi(self, data):
        """
        利用动态规划来解决隐式马尔科夫的预测问题
        """
        data_len = len(data)
        delta = np.zeros((data_len, WORD_TYPES))
        pre = delta.copy()

        # 初始化
        for i in range(WORD_TYPES):
            delta[0][i] = self.pi_list[i] + self.b[i][ord(data[0])]

        # 构建delta 和 pre
        for index in range(1, data_len):
            for typ in range(WORD_TYPES):
                val_list = [
                    delta[index - 1][WORD_HEAD] + self.a[WORD_HEAD][typ],
                    delta[index - 1][WORD_MIDDLE] + self.a[WORD_MIDDLE][typ],
                    delta[index - 1][WORD_END] + self.a[WORD_END][typ],
                    delta[index - 1][WORD_SINGLE] + self.a[WORD_SINGLE][typ]
                ]

                delta[index][typ] = max(val_list) + self.b[typ][ord(data[index])]
                pre[index][typ] = val_list.index(max(val_list))

        # 找出最后位置的最大值是哪一个状态
        [[last_max_index]] = np.argwhere(delta[data_len - 1] == max(delta[data_len - 1]))
        last_max_index = int(last_max_index)

        # 状态列表
        decode_list = [-1] * data_len
        decode_list[-1] = last_max_index

        pre_max_index = last_max_index
        for i in range(data_len - 1, 1, -1):
            pre_max_index = pre[i][pre_max_index]
            pre_max_index = int(pre_max_index)
            decode_list[i - 1] = pre_max_index

        return decode_list

    def _create_segment(self,data,decode):
        decode_data = unicode('')
        for index, value in enumerate(data):
            decode_data += value
            if decode[index] in (WORD_END,WORD_SINGLE):
                decode_data += '|'
        return decode_data

    def _save(self):
        with open('pi.pkl', 'wb') as f:
            pickle.dump(self.pi_list, f)

        with open('a.pkl', 'wb') as f:
            pickle.dump(self.a, f)

        with open('b.pkl', 'wb') as f:
            pickle.dump(self.b, f)

    def _log_normalize(self, a):
        s = 0
        for x in a:
            s += x
        if s == 0:
            print ("Error..from log_normalize.")
            return
        s = math.log(s)
        for i in range(len(a)):
            if a[i] == 0:
                a[i] = INFINITE
            else:
                a[i] = math.log(a[i]) - s

    def _train(self, words):

        last_q = WORD_END
        for k, word in enumerate(words):
            word = word.strip()
            n = len(word)
            # print word,len(word)

            if n <= 0:
                continue
            elif n == 1:
                self.pi_list[WORD_SINGLE] += 1
                self.a[last_q][WORD_SINGLE] += 1  # 上一个词的结束到当前状态
                self.b[WORD_SINGLE][ord(word[0])] += 1
                last_q = WORD_SINGLE
                continue
            else:
                self.pi_list[WORD_HEAD] += 1
                self.pi_list[WORD_END] += 1
                self.pi_list[WORD_MIDDLE] += (n - 2)

                self.a[last_q][WORD_HEAD] += 1
                last_q = WORD_END

                if n == 2:
                    self.a[WORD_HEAD][WORD_HEAD] += 1
                else:
                    self.a[WORD_HEAD][WORD_MIDDLE] += 1
                    self.a[WORD_MIDDLE][WORD_END] += 1
                    self.a[WORD_MIDDLE][WORD_MIDDLE] += (n - 3)

                self.b[WORD_HEAD][ord(word[0])] += 1
                self.b[WORD_END][ord(word[n - 1])] += 1
                for i in range(1, n - 1):
                    self.b[WORD_MIDDLE][ord(word[i])] += 1

        # 正则化
        self._log_normalize(self.pi_list)
        for i in range(WORD_TYPES):
            self._log_normalize(self.a[i])
            self._log_normalize(self.b[i])


if __name__ == '__main__':
    file = u'pku_training.utf8'
    hmm = DiscreteHMM()
    hmm.train(file)
    decode =  hmm.segment('novel.txt')
    with open('decode_novel.txt','wb') as f:
        f.write(decode)
