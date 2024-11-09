import formulas as fm
import file_parser as fp

def main():
    n = 3
    print("Starting... using {}".format(n))
    print("Calculated square root : {}".format(fm.sqrt(n)))
    print("Incrementing {} ... : ".format(n), fm.increment(n))
    print("Decrementing {} ... : ".format(n), fm.decrement(n))
    print("Calculated square : {}".format(fm.square(n)))
    print("Ran...")
    print("We can add additional prints afterwards, not triggered by pytest if not defined ... (y)")

    fcsv = fp.read_file('./tests/data/input.csv')
    data = fp.parse(data=fcsv, n=1)
    print("data.csv file written successfully : ", fp.write_file('data.csv', data=data))

if __name__ == "__main__":
    main()