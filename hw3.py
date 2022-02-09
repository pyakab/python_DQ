problem_string = '''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''


def count_whitespace():
    a = 0
    count = 0
    while a < len(problem_string):
        if problem_string[a].isspace():
        #if problem_string[a] == " " or problem_string[a] == "\n" or problem_string[a] == "\t":
            count = count + 1
        a = a + 1
    return f"Number of whitespace is {count}."


def make_lowercase_letter():
    global lower_problem_string
    lower_problem_string = problem_string.lower()
    return lower_problem_string


def create_new_sentence():
    newstring = []
    tested_string1 = lower_problem_string.split('.')
    x = 0

    while x < len(tested_string1):
        temp_string = ""
        last_string = temp_string.join(tested_string1[x])
        lis = list(last_string.split(" "))
        lenght = len(lis)
        newstring.append(lis[lenght - 1])
        x = x + 1

    last_sentence = " "
    last_sentence1 = last_sentence.join(newstring)
    global tested_string2
    tested_string2 = lower_problem_string + ' ' + last_sentence1 + '.'


def normalize_text():
    formatted_string = []
    global formatted_string1
    formatted_string1 = []
    x = 0
    while x < len(tested_string2):
        if tested_string2[x] == "\n" and tested_string2[x + 1] == "\n":
            pass
        elif tested_string2[x] == " " and tested_string2[x + 1] == " ":
            pass
        elif tested_string2[x] == " " and tested_string2[x + 1] == ".":
            pass
        elif tested_string2[x - 1] == "\n" and tested_string2[x] == "\t":
            pass
        elif tested_string2[x] == " " and tested_string2[x - 1] == "." and tested_string2[x + 1] == "\n":
            pass
        elif tested_string2[x] == '“' and tested_string2[x - 1] != " ":
            formatted_string.append(' ')
            formatted_string.append(tested_string2[x])
        elif tested_string2[x - 2] == " " and tested_string2[x - 1] == "i" and tested_string2[x] == "z" and \
                tested_string2[x + 1] == " ":
            formatted_string.append('s')
        else:
            formatted_string.append(tested_string2[x])

        x = x + 1

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


def create_string_from_list():
    s1 = ""
    final_formatted_string = s1.join(formatted_string1)
    return final_formatted_string


count_whitespace()
make_lowercase_letter()
create_new_sentence()
normalize_text()
create_string_from_list()
print(count_whitespace())
print(create_string_from_list())
