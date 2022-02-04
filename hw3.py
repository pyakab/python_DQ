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
print(lower_problem_string)

formatted_string = []
formatted_string1 = []


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


def listToString(formatted_string1):
    # initialize an empty string
    s1 = ""
    final_formatted_string = s1.join(formatted_string1)
    print(final_formatted_string)

    # print(splitted_string[a])


# words = lower_problem_string.split()
# last_word=lower_problem_string.rfind('.')
# last_word =re.findall(r'*?.',lower_problem_string)
# print(last_word)
# if words[-2] == ' *[.]':
#    last_word = words[-1]
#    print(last_word)


# def normalize_text():
# result = re.search(r'*?. ', lower_problem_string)
# print(result)
# word_string = lower_problem_string.split()
# print(word_string)
# i=1
# while i < len(word_string):
#    if word_string[i-1]=='*.':
#        print(word_string[i-1])
#        lower_problem_string[i].upper()
#    i = i+1
#    if splitted_string[a] == ' iz ':
#        problem_string.replace(' iz ', ' is ')
#    else:
#        pass

# print(lower_problem_string)


count_whitespace()
new_sentence()
# normalize_text()
listToString(formatted_string1)
