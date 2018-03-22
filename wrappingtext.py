"""
textwrap.wrap() will produce a list elemnts
of type string that are MAX 70 characters
long by default. It will break at nearest space
textwrap.fill() is similar only instead o list it will
produce  a string 
"""

import textwrap

def main():
    path_to_file = raw_input("Enter path to file: " )
    fobr = open(path_to_file,"r")
    longstring = fobr.read()
    print longstring
    wrapped_str = textwrap.wrap(longstring)
    for line in wrapped_str:
        print len(line),line
    fobr.close()


if __name__ == "__main__":
    main ()
