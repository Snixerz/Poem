import random

poem = '''If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer…
If you’re a pretender, come sit by my fire
For we have some flax-golden tales to spin.
Come in!
Come in!'''

x = poem.split()

def lines_printed_backward(lines_list):
    '''pass'''
    #TODO: reverse the list 
    lines_list.reverse()
    print(lines_list)

    #TODO: use loop to print out items in list
    for i in lines_list:
        print(i)
    pass

def lines_printed_random(lines_list):
    poem_in_list = lines_list.copy()

    random.shuffle(poem_in_list)
    for i in poem_in_list:
        print(i)

lines_list = poem.split("\n")
lines_printed_random(lines_list)
