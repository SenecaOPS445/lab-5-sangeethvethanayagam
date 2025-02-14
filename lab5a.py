#!/usr/bin/env python3
# Author ID: SVETHANAYAGAM3

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open('data.txt', 'r')
    return f.read()


#def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters

if __name__ == '__main__':

    file_name = 'data.txt'
    print(read_file_string(file_name))
    #print(read_file_list(file_name))