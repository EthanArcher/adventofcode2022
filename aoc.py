import string


def read_input(filename, datatype=str, sep='\n'):
    with open(f"inputs/{filename}.txt") as f:
        contents = f.read().strip().split(sep)
        return list(map(datatype, contents))


def read_input_line(filename, sep=''):
    filename = f"{filename:02d}" if isinstance(filename, int) else filename
    with open(f"inputs/{filename}.txt") as f:
        contents = f.read().strip()
        return contents if not sep else contents.split(sep)


alphabet = dict(zip(string.ascii_lowercase, range(1,27))) | dict(zip(string.ascii_uppercase, range(27,53)))
