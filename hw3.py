import re

problem_string = '''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''


def count_whitespace():
    a = 0
    count = 0
    while a < len(problem_string):
        # print(splitted_string[a])

        if problem_string[a] == " " or problem_string[a] == "\n" or problem_string[a] == "\t":
            count = count + 1
        a = a + 1
    print(count)


lower_problem_string = problem_string.lower()
lower_problem_string1=(lower_problem_string.split())

formatted_string = []
formatted_string1 = []

def create_last_sentence():
    match = ''
    match = re.match('[a-zA-Z0-9.]', lower_problem_string)
    print(match)


def new_sentence():
    x = 0
    while x < len(lower_problem_string):
        if lower_problem_string[x] == "\n" and lower_problem_string[x + 1] == "\n":
            pass
        elif lower_problem_string[x] == " " and lower_problem_string[x + 1] == " ":
            pass
        elif lower_problem_string[x - 1] == "\n" and lower_problem_string[x] == "\t":
            pass
        elif lower_problem_string[x] == " " and lower_problem_string[x - 1] == "." and lower_problem_string[
            x + 1] == "\n":
            pass
        elif lower_problem_string[x - 2] == " " and lower_problem_string[x - 1] == "i" and lower_problem_string[
            x] == "z" and lower_problem_string[x + 1] == " ":
            formatted_string.append('s')
        else:
            formatted_string.append(lower_problem_string[x])

        x = x + 1
    print(formatted_string)

    y = 0

    while y < len(formatted_string):
        if formatted_string[y - 2] == ":" and formatted_string[y - 1] == "\n":
            formatted_string1.append(formatted_string[y].upper())
        elif formatted_string[y - 2] == "." and formatted_string[y - 1] == " ":
            formatted_string1.append(formatted_string[y].upper())
        elif formatted_string[y - 2] == "." and formatted_string[y - 1] == "\n":
            formatted_string1.append(formatted_string[y].upper())
        elif y == 0:
            formatted_string1.append(formatted_string[y].upper())
        else:
            formatted_string1.append(formatted_string[y])

        y = y + 1

    print(formatted_string1)


def create_string_from_list():
    # initialize an empty string
    s1 = ""
    global final_formatted_string
    final_formatted_string = s1.join(formatted_string1)
    #print(final_formatted_string)

#def create_last_sentence():
#    newsentence = ""

    # calculating length of string
    #final_formatted_string1 = list(final_formatted_string.split(" "))

    #length = len(final_formatted_string1)

    #print(final_formatted_string1)

    # traversing from last
    #for i in range(length - 1, 0, -1):

        # if space is occurred then return
     #   if (final_formatted_string[i] == "."):

            # return reverse of newstring
      #      return newsentence[::-1]
       # else:
        #    newsentence = newsentence + final_formatted_string[i]

    #print(newsentence)
    #test=final_formatted_string.split

    #before, term, after = final_formatted_string.partition(':')
    #before = before.rsplit(maxsplit=2)[-1:]

    #for i in final_formatted_string:
    #    if re.search(r"([a-zA-Z]+).", final_formatted_string):






count_whitespace()
create_last_sentence()
new_sentence()
# normalize_text()
create_string_from_list()

