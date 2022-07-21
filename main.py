from helpers import *
import sys
if __name__ == '__main__':
    #print(get_files_path(extension='.txt'))
    try:
        str_to_find = sys.argv[1]
        find_word_in_files(str_to_find=str_to_find)
    except IndexError:
        print('Please provide an argument in the execution!\n'
              'Example: python main.py foo')
    #display text in different colour - ansi colours (put extra chars before and after what we want to highlight
    #print("\033[93mThis is red!\033[0m")
    #print(sys.argv)
