#!/usr/bin/python
# -*- coding: utf-8 -*-


def generate_array(array,dest):
    count = len(array)
    temp_list = []
    for i in range(0,len(array)):
        if i %2 == 0:
            dest.append(array[i])
        else:
            temp_list.append(array[i])
    if len(temp_list) > 1:

        if count % 2 != 0:
            temp_list.append(temp_list[0])
            temp_list = temp_list[1:]

        generate_array(temp_list,dest)
    else:
        dest.extend(temp_list)




if __name__ == '__main__':
    a = [0,1,2,3,4,5,6]
    b = [17,13,11,2,3,5,7]
    b= sorted(b)
    dest = []

    generate_array(a,dest)
    print ("dest: ", dest)


    c = [0]*len(a)
    print ("b: ", b)
    for i in range(len(a)):
        c[dest[i]] = b[i]

    print ("c: ", c)


    # dest2=[]
    # generate_array(c,dest2)
    # print (dest2)

