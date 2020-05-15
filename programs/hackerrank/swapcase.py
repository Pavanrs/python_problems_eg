"""
Function to swap case (upper case to lower case and vice versa)
Example: Input: 'Hello' -> Output: 'hELLO'
"""


def swap_case(s):
    if s is None:
        return None

    new_s = ''
    for i in s:
        if i.isupper():
            j = i.lower()
        else:
            j = i.upper()

        new_s = new_s + j
    return new_s

if __name__ == "__main__":
    print("In swapcase.py")
    str_input = "Hello"
    str_output = swap_case(str_input)
    print("Input:[{}]".format(str_input))
    print("Output:[{}]".format(str_output))