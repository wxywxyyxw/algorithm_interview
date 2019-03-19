import random
import itertools

def allocate_strategy(user_id_list, review_num):

    #random.shuffle(user_id_list)
    review_user_count = int(review_num) + 1
    review_list = []

    if review_num == 1:
        for i in range(len(user_id_list)):
            if i != len(user_id_list) -1:
                review_list.append((user_id_list[i],user_id_list[i+1]))
            else:
                review_list.append((user_id_list[i],user_id_list[0]))
    else:
        for i in range(len(user_id_list) / review_user_count):

            review_list.extend(list(
                itertools.permutations(user_id_list[review_user_count * i:review_user_count * (i + 1)], 2)))

            if i == len(user_id_list) / review_user_count - 1 and len(user_id_list) % review_user_count != 0:

                if len(user_id_list) % review_user_count  == 1:
                    random_item = random.randint(0,len(review_list)-1)
                    random_tuple = review_list[random_item]

                    review_list[random_item] = (user_id_list[-1],random_tuple[1])

                review_list.extend(
                    [item for item in list(itertools.permutations(user_id_list[-1 * review_user_count:], 2)) if
                     item[1] not in user_id_list[:review_user_count * (i + 1)]])



        #print (review_list)

    return review_list

print (allocate_strategy([1,2,3,4],2))