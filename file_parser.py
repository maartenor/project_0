import csv
import formulas as fm

def read_file(filename):
    with open(filename) as f:
        data = f.readlines()
        f.close()
    return data

def parse(data, n=1):
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
    try:
        with open(filename, 'w') as f:
            f.writelines(data)
        
        f.close()
        
        return True
    except:
        return False