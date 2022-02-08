import random  # import random library
from random import randint, choice  # import library for creating random list
import string  # import string library
import collections  # import collections library


random_dict_list = []
duplicates = []
key_list = []
one_common_list = {}



def create_random_collection():  # define the method for creating the list of 10 random dictionaries
    letters = ""
    letters = string.ascii_lowercase  # initialized string of lowercase letters
    global random_dict_list
    for i in range(0, 10):  # set the conditions of the loop
        x = 0  # initialize the x variable, which will be used in the loop
        random_dict = {}  # initialize the dictionary
        while x < 10 and len(random_dict) < 10:  # set the conditions of the loop
            letter_key = random.choice(letters)  # choose any letter from the string of lowercase letters
            n = randint(0, 100)  # initialize the variable n in the range from 1 to 100 with the randint function
            random_dict[letter_key] = n  # add item (key and value) to the dictionary
            x = x + 1  # increase the counter x
        random_dict_list.append(random_dict)  # add created dictionary to the list
    return random_dict_list


def create_key_list():  # define the method for creating the common dictionary
    global key_list
    i = 0  # initialize the i variable, which will be used in the loop
    while i < len(random_dict_list):  # set the conditions of the loop
        tested_dictionary = random_dict_list[i]  # set tested_dictionary = [i] dictionary from the random_dict_list
        for key in tested_dictionary:  # set the conditions of the loop
            key_list.append(key)  # add the key from the dictionary to the list of keys
        i = i + 1  # increase the counter i
    return key_list


def create_duplicates_list():
    global duplicates
    duplicates = [item for item, count in collections.Counter(key_list).items() if count > 1]  # add to the duplicates list keys that are repeated in the key_list
    return duplicates


def create_common_dictionary():
    uniq = set(key_list)  # clear the key_list from duplicates

    if len(duplicates) <= 0:  # the condition for checking if duplicates list is empty
        one_common_list = {}  # initialize list for the all keys in the random_dict_list

        y = 0  # initialize the y variable, which will be used in the loop
        while y < len(random_dict_list):  # set the conditions of the loop
            tested_dictionary = random_dict_list[y]  # set tested_dictionary = [y] dictionary from the random_dict_list
            for z in uniq:  # set the conditions of the loop
                if z in tested_dictionary:  # the condition for checking if keys is in the [y] dictionary
                    one_common_list[z] = tested_dictionary[z]  # add item (key and value) to the one_common_list dictionary

            y = y + 1  # # increase the counter y

    else:  # if condition is false
        clear_uniq = []  # initialize list for unique keys
        for x in uniq:  # set the condition of the loop
            if x not in duplicates:  # the condition for checking if key is in the duplicates list
                clear_uniq.append(x)  # if condition is true, add key to the clear_uniq list
            else:  # if condition is false
                pass  # do nothing
        one_common_list = {}  # initialize list for the all keys in the random_dict_list

        y = 0  # initialize the y variable, which will be used in the loop
        while y < len(random_dict_list):  # set the condition of the loop
            tested_dictionary = random_dict_list[y]  # set tested_dictionary = [y] dictionary from the random_dict_list
            for z in clear_uniq:  # set the condition of the loop
                if z in tested_dictionary:  # the condition for checking if keys is in the [y] dictionary
                    one_common_list[z] = tested_dictionary[z]  # add item (key and value) to the one_common_list dictionary

            y = y + 1  # increase the counter y

        for m in duplicates:  # set the condition of the loop
            duplicate_list = {}  # initialize the dictionary for the repeated key
            k = 0  # initialize the k variable, which will be used in the loop

            while k < len(random_dict_list):  # set the condition of the loop
                if m in random_dict_list[k]:  # the condition for checking if key is in the k-dictionary in the random_dict_list
                    tested_dictionary = random_dict_list[k]  # set tested_dictionary = [y] dictionary from the random_dict_list
                    final_key_name = str(m) + "_" + str(k + 1)  # set the final_key_name as concat m and (k+1) variables
                    duplicate_list[final_key_name] = tested_dictionary[m]  # add item (key and value) to the one_common_list dictionary

                else:  # if condition is false
                    pass  # do nothing

                k = k + 1  # increase the counter k
                if k == len(random_dict_list):  # check if the k = the length of list
                    biggest_key = max(duplicate_list,key=duplicate_list.get)  # get the key with the biggest value from the duplicate_list dictionary
                    # print(biggest_key)
                    one_common_list[biggest_key] = duplicate_list[biggest_key]  # add item (key and value) to the one_common_list dictionary
                    # print(one_common_list)
                else:  # if condition is false
                    pass  # do nothing

    if len(uniq) == len(one_common_list):  # check if the count of elements in the received list = count in the uniq
        return one_common_list  # print the one_common_list in console
    else:  # if condition is false
        return 'Houston, we have a problem!'  # print the message about the error in console


create_random_collection()  # call the method create_random_collection
create_key_list()
create_duplicates_list()
create_common_dictionary()  # call the method create_common_dictionary
print(create_random_collection())
print(create_common_dictionary())
