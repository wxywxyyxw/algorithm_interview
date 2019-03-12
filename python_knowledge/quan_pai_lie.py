import itertools
import random

def allocate_strategy(user_id_list, review_num):
        random.shuffle(user_id_list)
        print (user_id_list)
        review_user_count = review_num + 1
        review_list = []
        for i in range(int(len(user_id_list)/review_user_count)):
            review_list.extend(list(
                itertools.permutations(user_id_list[review_user_count * i:review_user_count * (i + 1)], 2)))
            if i == review_user_count - 1 and len(user_id_list) % review_user_count != 0:
                review_list.extend(
                    [item for item in list(itertools.permutations(user_id_list[-1 * review_user_count:], 2)) if
                     item[1] not in user_id_list[:review_user_count * (i + 1)]])

        return review_list



if __name__ == '__main__':
    result = allocate_strategy([1,2,3,4,5,6,7,8,9,10,11,12],2)
    #result = allocate_strategy([8,9,10],2)
    print (len(result), result)
