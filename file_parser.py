import formulas as fm

def read_file(filename):
    """
    Reads content from a file and returns it as a list of lines.

    Args:
        filename (str): Path to the file to be read

    Returns:
        list: List containing lines from the file

    Raises:
        FileNotFoundError: If the specified file doesn't exist
        IOError: If there's an error reading the file
    """
    with open(filename) as f:
        data = f.readlines()
        f.close()
    return data

def parse(data, n=1):
    """
    Processes input data by squaring numbers and multiplying by a factor.
    
    Args:
        data (str or list): Input data to be processed. Can be either a string
            that will be split into words or a list of values
        n (int, optional): Multiplication factor to apply after squaring. Defaults to 1

    Returns:
        str: A string containing processed values, one per line. 
            'ERR' is returned for values that cannot be processed

    Examples:
        >>> parse("1 2 3", 2)
        "2\n8\n18\n"
        >>> parse(["1", "a", "2"])
        "1\nERR\n4\n"
    """
    updated = ""
    if isinstance(data, str):
        data = data.split()
    for line in data:
        try:
            line = str( fm.square(int(line)) * n )
        except:
            line = 'ERR'
        updated += line+'\n'
    return updated

def write_file(filename, data):
    """
    Writes data to a file.

    Args:
        filename (str): Path to the file where data will be written
        data (str): Content to write to the file

    Returns:
        bool: True if write operation was successful, False otherwise

    Raises:
        IOError: If there's an error writing to the file
        PermissionError: If the program lacks permission to write to the file
    """
    try:
        with open(filename, 'w') as f:
            f.writelines(data)
        
        f.close()
        
        return True
    except:
        return False