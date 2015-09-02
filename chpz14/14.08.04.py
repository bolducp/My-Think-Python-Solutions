"""In a large collection of MP3 files, there may be more than one copy
of the same song, stored in different directories or with different file
names. The goal of this exercise is to search for duplicates.
Write a program that searches a directory and all of its subdirectories,
recursively, and returns a list of complete paths for all files with a
given suffix (like .mp3). Hint: os.path provides several useful functions
for manipulating file and path names.
To recognize duplicates, you can use md5sum to compute a “checksum” for
each files. If two files have the same checksum, they probably have the
same contents."""


import os

def get_mp3_files(dirname):
    mp3_files = []
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            if filename[-4:] == ".mp3":
                mp3_files.append(os.path.join(root, filename))
    return mp3_files


def check_duplicates(list_files):
    checksum_dict = {}

    for a_file in list_files:
        checksum = os.open('md5sum ' + a_file)
        res = checksum.read()
        checksum.close()

        if res in checksum_dict:
            print "There's a duplicate!"
            print a_file + " \ " + checksum_dict[res]
        else:
            checksum_dict[res] = a_file


sample_files = get_mp3_files("c:\users\admin\downloads")
check_duplicates(sample_files)


