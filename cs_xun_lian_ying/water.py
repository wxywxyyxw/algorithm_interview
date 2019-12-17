#!/usr/bin/env python3
a_size, b_size, c_size = 80, 50, 30
a, b, c = 80, 0, 0


def change_water(x, y, x_size, y_size):
    if x >= y_size - y:
        return x - (y_size - y), y_size
    else:
        return 0, x + y


def water(a, b, c, flag, route, tag):
    #print(a, b, c, flag, route)

    if a == 40 and b == 40 and c == 0:
        #print('find !!!!!!!!')
        return tag

    if a > 0:
        if b < b_size:
            aa, bb = change_water(a, b, a_size, b_size)
            #print ('a b',aa,bb)

            if (aa, bb, c) not in route:

                route.append((aa, bb, c))
                tag.append('A B')
                ret = water(aa, bb, c, flag + 1, route,tag)

                if ret == '0':
                    route.pop()
                    tag.pop()
                else:
                    return ret

        if c < c_size:

            aa, cc = change_water(a, c, a_size, c_size)
            #print ('a c',a,c)


            if (aa, b, cc) not in route:

                route.append((aa, b, cc))
                tag.append('A C')
                ret = water(aa, b, cc, flag + 1, route,tag)

                if ret == '0':
                    route.pop()
                    tag.pop()
                else:
                    return ret


    if b > 0:
        if a < a_size:
            bb, aa = change_water(b, a, b_size, a_size)
            #print ('b a',bb,aa)
            if (a, bb, c) not in route:
                route.append((aa, bb, c))
                tag.append('B A')
                ret = water(aa, bb, c, flag + 1, route,tag)

                if ret == '0':
                    route.pop()
                    tag.pop()
                else:
                    return ret

        if c < c_size:

            bb, cc = change_water(b, c, b_size, c_size)
            #print ('b c',bb,cc)
            if (a, bb, cc) not in route:

                route.append((a, bb, cc))
                tag.append('B C')
                ret = water(a, bb, cc, flag + 1, route,tag)

                if ret == '0':
                    route.pop()
                    tag.pop()
                else:
                    return ret

    if c > 0:
        if a < a_size:
            cc, aa = change_water(c, a, c_size, a_size)
            #print ('c a',cc,aa)
            if (aa, b, cc) not in route:

                route.append((aa, b, cc))
                tag.append('C A')
                ret = water(aa, b, cc, flag + 1, route,tag)

                if ret == '0':
                    route.pop()
                    tag.pop()
                else:
                    return ret

        if b < b_size:

            cc, bb = change_water(c, b, c_size, b_size)
            #print ('c b',cc,bb)
            if (a, bb, cc) not in route:

                route.append((a, bb, cc))
                tag.append('C B')
                ret = water(a, bb, cc, flag + 1, route,tag)

                if ret == '0':
                    route.pop()
                    tag.pop()

                else:
                    return ret

    return '0'


tag = water(80, 0, 0, 0, [(80, 0, 0)],[])

print (len(tag))
for item in tag:
    print (item)

