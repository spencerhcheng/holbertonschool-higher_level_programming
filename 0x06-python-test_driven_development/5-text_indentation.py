#!/usr/bin/python3
def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ['.', '?', ':']:
        if char in text:
            text = text.replace(char, char + "@")

    new_list = text.split('@')

    for idx in range(len(new_list)):
        if new_list[idx] == "":
            del new_list[idx]

    for idx, line in enumerate(new_list):
        new_list[idx] = line.strip()

    new_str = ('\n\n'.join(new_list))

    if new_str[-1] == '.' or new_str[-1] == '?' or new_str[-1] == ':':
        new_str += '\n'

    print(new_str)
