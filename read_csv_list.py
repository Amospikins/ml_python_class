def read_csv_lines(path='data.csv'):
    """Return a list where each element is one line from the CSV file.

    Lines are returned without trailing newline characters.
    """
    with open(path, 'r', encoding='utf-8') as f:
        return [line.rstrip('\r\n') for line in f]


if __name__ == '__main__':
    lines = read_csv_lines('data.csv')
    print(lines)
