"""
This file __main__.py is needed when a directory is provided as a parameter to python command instead .py file

> python3.7 -m programs
"""

from programs.hackerrank.swapcase import swap_case

if __name__ == "__main__":
    print("In __main__.py")
    str_input = "Hello"
    str_output = swap_case(str_input)
    print("Input:[{}]".format(str_input))
    print("Output:[{}]".format(str_output))