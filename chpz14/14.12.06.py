"""The urllib module provides methods for manipulating URLs and downloading information from the web.
The following example downloads and prints a secret message from thinkpython.com:

import urllib

conn = urllib.urlopen('http://thinkpython.com/secret.html')
for line in conn:
    print line.strip()
Run this code and follow the instructions you see there."""

import urllib

#conn = urllib.urlopen('http://thinkpython.com/secret.html')

#for line in conn:
    #print line.strip()


def print_city_name_and_pop():

    user_input = raw_input("enter a 5-digit zipcode")
    user_zipcode = urllib.urlopen('http://uszip.com/zip/' + user_input)

    lines = user_zipcode.readlines()

    name_line = lines[7]
    name = name_line[7: -17]

    text = ''

    for line in lines:
        new_line = line.strip()
        for word in new_line:
            text += word

    pop_index = text.find("Total population") + 25
    pop_end_index = text.find("<", pop_index)
    pop_text = text[pop_index: pop_end_index]


    print "The population of %s is %s" % (name, pop_text)

print_city_name_and_pop()




