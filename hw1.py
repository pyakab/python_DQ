from random import randint  # import library for creating random list

randomlist = []  # initialize the list
sorted_randomlist = []  # initialize the list
avg_list = []  # initialize the list


def create_100_elements_list():  # define the function(method) for creating the list of 100 random numbers
    i = 0  # initialize the i variable, which will be used in the loop
    while i < 100:  # set the conditions of the loop
        n = randint(1, 1000)  # initialized the variable n in the range from 1 to 1000 with the randint function
        randomlist.append(n)  # add the n variable to the list
        i = i + 1  # increment


def sort_list_elements(list):  # define the function for sorting the the list of 100 random numbers
    global sorted_randomlist  # set the global variable for using it in the other functions
    sorted_randomlist = list  # set the sorted_randomlist is equal to the input list
    i = 0  # initialize a variable for the loop
    while i <= len(sorted_randomlist):  # set the conditions for the exit from the loop after checking all elements in the list
        j = 0  # initialize a variable for the loop
        while j < len(sorted_randomlist) - i - 1:  # set the conditions for the exit from the loop
            if sorted_randomlist[j] > sorted_randomlist[j + 1]:  # set the condition for checking if the element with index i is bigger than element i+1
                sorted_randomlist[j], sorted_randomlist[j + 1] = sorted_randomlist[j + 1], sorted_randomlist[j]  # change the indexes of i and i+1 elements, it condition is true
            else:  # if the condition is false, do next
                j = j + 1  # increase the variable j by 1
        i = i + 1  # increase the variable j by 1


def calculate_average(list):  # define the name of the function for calculating the average for odd and even numbers
    global avg_list  # initializing the global variable
    avg_list = list  # set the variable equal to the received list
    i = 0  # set the variable (counter) i equal to the 0
    even_sum = 0  # initialize the even_sum variable
    even_count = 0  # initialize the even_count variable
    odd_sum = 0  # initialize the odd_sum variable
    odd_count = 0  # initialize the odd_count variable
    while i < len(avg_list):
        if avg_list[i] % 2 == 0:  # the condition for checking if element with index i in the list is even
            even_sum = even_sum + avg_list[i]  # the element is added to the even_sum, if the condition is true
            even_count = even_count + 1  # count of even_element is increased by 1, if condition is true
            i = i + 1  # increase the counter
        else:  # when condition is false, next
            odd_sum = odd_sum + avg_list[i]  # the element is added to the odd_sum, if the condition is false
            odd_count = odd_count + 1  # count of odd_element is increased by 1, if condition is false
            i = i + 1  # increase the counter
    even_avg = even_sum / even_count  # when the loop is end, count the average of even numbers
    odd_avg = odd_sum / odd_count  # when the loop is end, count the average of odd numbers
    print(even_avg)  # print the even_avg in console
    print(odd_avg)  # print the odd_avg in console


create_100_elements_list()  # call the method create_100_elements_list
sort_list_elements(randomlist)  # call the method sort_list_elements with the input variable randomlist
calculate_average(sorted_randomlist)  # call the method calculate_average with the input variable sorted_randomlist
