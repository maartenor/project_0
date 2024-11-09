import formulas as fm

def main():
    n = 3
    print("Starting... using {}".format(n))
    print("Calculated square root : {}".format(fm.sqrt(n)))
    print("Incrementing {} ... : ".format(n), fm.increment(n))
    print("Decrementing {} ... : ".format(n), fm.decrement(n))
    print("Calculated square : {}".format(fm.square(n)))
    print("Ran...")
    print("We can add additional prints afterwards, not triggered by pytest if not defined ... (y)")

if __name__ == "__main__":
    main()