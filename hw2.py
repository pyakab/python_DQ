import random
from random import randint, choice  # import library for creating random list
import string
import collections

# 1. create a list of random number of dicts (from 2 to 10)

# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
# 2. get previously generated list of dicts and create one common dict:

# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# Each line of code should be commented with description.
random_dict_list=[]

def create_random_collection():
    key_list=[]
    value_list=[]
    letters = string.ascii_lowercase
    for i in range (0,10):
        x = 0
        random_dict={}
        while x <10 and len(random_dict)<10:
            letter_key = random.choice(letters)
            n=randint(0, 100)
            random_dict[letter_key]=n
            x = x + 1
        random_dict_list.append(random_dict)
        i=i+1
    print(len(random_dict_list))


def create_common_dictionary(list):
    print(random_dict_list)
    i=0
    key_list = []
    tested_dictionary={}

    while i<len(random_dict_list):
        tested_dictionary=random_dict_list[i]
        for key in tested_dictionary:
            #print(tested_dictionary.items())
            #y=1
            #while y<len(tested_dictionary_list):
            #    if tested_dictionary.items() not in
            key_list.append(key)
            #if key not in key_list:
            #    key_list.append(key)
            #else:
            #    pass
        i=i+1
    print(key_list)
    print(len(key_list))

    duplicates = [item for item, count in collections.Counter(key_list).items() if count > 1]
    print(duplicates)
    print(len(duplicates))
    uniq = set(key_list)
    #print(uniq)
    print(len(uniq))

    if len(duplicates) <= 0:
        one_common_list = {}

        y = 0
        while y < len(random_dict_list):
            tested_dictionary = random_dict_list[y]
            for z in uniq:
                if z in tested_dictionary:
                    one_common_list[z] = tested_dictionary[z]
                    print(one_common_list)
            y = y + 1

    else:
        clear_uniq=[]
        for x in uniq:
            if x not in duplicates:
                clear_uniq.append(x)
            else:
                pass
        one_common_list = {}

        y = 0
        while y<len(random_dict_list):
            tested_dictionary=random_dict_list[y]
            for z in clear_uniq:
                if z in tested_dictionary:
                    one_common_list[z] = tested_dictionary[z]
                    print(one_common_list)
            y=y+1


        for m in duplicates:
            duplicate_list={}
            k = 0
            while k<len(random_dict_list):
                if m in random_dict_list[k]:
                    tested_dictionary=random_dict_list[k]
                    key_dict={}
                    key_one=1
                    final_key_name = str(m)+"_"+str(k+1)
                    #print(final_key_name)
                    key_dict[1] = final_key_name
                    print(key_dict[1])
                    duplicate_list[key_dict[1]] = tested_dictionary[m]
                    print(duplicate_list)
                    #if k+1==len(random_dict_list):
                    #    biggest_key=max(duplicate_list, key=duplicate_list.get)
                    #    print(biggest_key)
                    #    one_common_list[biggest_key] = duplicate_list[biggest_key]
                    #    print(one_common_list)
                    #else:
                    #    pass

                else:
                    pass

                k=k+1
                if k + 1 == len(random_dict_list):
                    biggest_key = max(duplicate_list, key=duplicate_list.get)
                    print(biggest_key)
                    one_common_list[biggest_key] = duplicate_list[biggest_key]
                    print(one_common_list)
                else:
                    pass



    #print(clear_uniq)
    print(len(uniq))
    print(len(one_common_list))
    print(one_common_list)



    #print([item for item, count in collections.Counter(key_list).items() if count > 1])

    #seen = set(key_list)
    #print(seen)
    #uniq = []
    #dupes = []

    #for x in key_list:
    #    if x in seen:

    #        dupes.append(x)
    #    else:
     #       pass

    #print(dupes)
    #print(seen)

#    one_common_list={}

#    for z in key_list:
#        y=0
#        while y<len(random_dict_list):
#            tested_dictionary = random_dict_list[z]
#            if z in tested_dictionary and z not in one_common_list:
#                one_common_list[z] = tested_dictionary[z]
#                print(one_common_list)



create_random_collection()
create_common_dictionary(random_dict_list)