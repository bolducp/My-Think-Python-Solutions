"""Write a function called sed that takes as arguments a pattern string,
a replacement string, and two filenames; it should read the first file
and write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the file, it should be replaced
with the replacement string.
If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message, and exit. """


def sed(pattern_str, replacement_str, file1, file2):
    try:
        fin = open(file1)
        lines = fin.readlines()

        new_file = open(file2, 'w')

        for line in lines:
            new_line = line.replace(pattern_str, replacement_str)
            new_file.write(new_line)

        new_file.close()
        new_file = open(file2)

        for line in new_file:
            print line

    except:
        print "Error"

