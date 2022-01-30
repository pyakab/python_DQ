import random
from random import randint, choice  # import library for creating random list
import string

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
    for i in range (0,3):
        x = 0
        random_dict={}
        while x <3 and len(random_dict)<3:
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
            print()
            if key not in key_list:
                key_list.append(key)
            else:
                pass
        #key_list.sort()
        print(key_list)
        print(len(key_list))

        one_common_list = {}
        for z in key_list:
            if z in tested_dictionary and z not in one_common_list:
                one_common_list[z]=tested_dictionary[z]
                print(one_common_list)
            elif z in tested_dictionary and z in one_common_list:
                print('change')
                if one_common_list[z]<tested_dictionary[z]:
                    print('bigger')
                    key_dict={}
                    key_one=1
                    final_key_name = str(z)+"_"+str(i)
                    key_dict[1]=final_key_name
                    #print(key_dict)
                    del one_common_list[z]
                    one_common_list[final_key_name] = tested_dictionary[z]
                else:
                    print('less')
                    key_dict = {}
                    key_one = 1
                    final_key_name = str(z) + "_" + str(i-1)
                    key_dict[1] = final_key_name
                    #print(key_dict)
                    one_common_list[final_key_name] = one_common_list[z]
                    del one_common_list[z]

                one_common_list[z]=tested_dictionary[z]

            else:
                #pass
                print(str(z) + ' not in dictionary ' + str(i))
            #print(one_common_list)
        i = i + 1
    print(one_common_list)
    print(key_list)
    print(len(key_list))

    print(len(one_common_list))

    #print(key_list)
    #num = 1
    one_common_list={}
    #for z in key_list:
        #print(z)
        #print(tested_dictionary[z])
        #while num < 3:
        #    if z in tested_dictionary:
        #        print(num)
        #        print(tested_dictionary[z])
                # one_common_list[z]=tested_dictionary[z]
        #    else:
        #        pass
        #    num=num+1


    """while num <=2:
        for z in key_list:
            if z in tested_dictionary:
                print(z)
                #one_common_list[z]=tested_dictionary[z]
            else:
                pass
        print(one_common_list)
        num=num+1
    print(one_common_list)"""

            #new_key=tested_dictionary.keys()
        #new_key=tested_dictionary.fromkeys(i)
        #print(new_key)
        #new_dictionary.append(new_key)

        #j=0
        #while j<len(tested_dictionary):
        #    k=j
        #    print(k)
        #    print(tested_dictionary[j])
        #    j=j+1




    #num = 1
    #one_common_list = {}
    #for z in key_list:
    #    while num <= 10:
    #        if z in tested_dictionary:
    #            print(dict.fromkeys(z))

            #else:
             #   print("Key does not exists in dictionary " + str(num))
            #num = num + 1








create_random_collection()
create_common_dictionary(random_dict_list)