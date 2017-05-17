#!/usr/bin/python3
def text_indentation(text):
    flag = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for x, ele in enumerate(text):
        if ((text[x] == '.' or text[x] == '?' or text[x] == ':') and (text[x + 1].isspace())):
            flag = 1
            x = x + 1
            print("{:s}\n".format(text[x]))

        elif ((text[x] == '.' or text[x] == '?' or text[x] == ':') and not (text[x + 1].isspace())):
            orubt("{:s}\n".format(text[x]))

        else:
            if flag == 1:
                x += 1
                print("{:s}".format(text[x]), end="")
            else:
                print("{:s}".format(text[x]), end="")
