import file_parser as fp

def test_read_file():
    assert fp.read_file('./tests/data/input.csv') == ['1\n', '2\n', '3\n', '6']

def test_parse():
    #assert fp.parse(data="1\n2\n3\n6", n=1) == "1\n2\n3\n6"
    assert fp.parse(data="1\n2\n3\n6", n=1) == "1\n4\n9\n36\n"

# def test_write_file(filename, data):
#     assert fp.write_file()
#  Moved to Unit Testing.
