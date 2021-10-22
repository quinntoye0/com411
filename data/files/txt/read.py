def display_chars(fileName, chars):
    with open(fileName) as file:
        partial_data = file.read(chars)
        print(partial_data)


def display_line(fileName):
    with open(fileName) as file:
        line = file.readline().strip()
        print(line)


def display_text(fileName):
    with open(fileName) as file:
        library = file.read()
        lines = library.split('\n')
        print(lines)


fileName = "library.txt"

display_chars(fileName, 10)
display_line(fileName)
display_text(fileName)

