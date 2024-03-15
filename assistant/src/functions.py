import re
from tabulate import tabulate


def get_multiline_string(input_str: str, n: int) -> str:
    """Function that converts one line long
        string into multilines string by inserting
        new line separator after next end of word
        after n sybmols

    Args:
        input_str (str): long sting to convert
        n (int): desired min number of symbols on 1 line

    Returns:
        str: multiline version of long str
    """
    if not isinstance(input_str, str):
        return input_str
    if len(input_str) <= n:
        return input_str

    lines = []
    start_index = 0

    while start_index < len(input_str):
        end_index = start_index + n

        # Find the next closest space or punctuation after n characters
        # Adjust the punctuation characters as needed
        next_break_index = re.search(r'[ .,;:!?)]|$', input_str[end_index:])

        if next_break_index:
            break_char_index = next_break_index.start()
            end_index += break_char_index + 1

            # Append the line to the list (excluding the punctuation character)
            lines.append(input_str[start_index:end_index].strip())
        else:
            # If no space or punctuation found, append the line as is
            lines.append(input_str[start_index:end_index].strip())

        # Move the start index to the next line
        start_index = end_index

    # Join the lines with newline characters
    return '\n'.join(lines)


def format_as_table(data: list, cell_width: int) -> str:
    """formats data to print as a table in cosole

    Args:
        data (list): list of dictionaries(key and values are strings), 
                     keys - name of columns, values - values for cells columns
        cell_width (int): desired min number of symbols for each value in 1 line

    Returns:
        str: string formatted as a table to print in console
    """
    new_data = []
    for dictionary in data:
        new_dict = {}
        for key, value in dictionary.items():
            get_multiline_string(value, cell_width)
            new_dict[key] = get_multiline_string(value, cell_width)
        new_data.append(new_dict)

    return tabulate(new_data, headers="keys", tablefmt="fancy_grid", numalign="center", stralign="left")


if __name__ == '__main__':

    data = [
        {"Name": "John", "Age": 30, "City": "New York"},
        {"Name": "Alice", "Age": 25, "City": "Los Angeles"},
        {"Name": "Bob", "Age": 35,
         "City": "This is a really long value that spans multiple) lines. This is a really long value (that) spans multiple lines. This is a really long value (that) spans multiple lines."},
    ]
    print(format_as_table(data, 40))
