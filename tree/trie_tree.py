#!/usr/bin/python
# -*- coding: utf-8 -*-

END = '$'

def make_trie(words):
    trie = {}
    for word in words:
        t = trie
        for c in word:
            if c not in t:
                t[c] = {}
                print (t)
            t = t[c]
            print (t)
        t[END] = {}
        print (t)
        break
    return trie

# 创建trie树
def create_trie(words):
    """
    利用字典来实现trie树，每个字符为一层key，最后一个字符包含一个$key, 比如说hello 就有6层key
    """
    trie = {}
    for word in words:
        temp_trie = trie
        for character in word:
            if character not in temp_trie:
                temp_trie[character] = {}
            temp_trie = temp_trie[character]
        temp_trie[END] = {}
    return trie


if __name__ == '__main__':
    words = ['hello', 'hela', 'dome']
    t = create_trie(words)
    print (t)
