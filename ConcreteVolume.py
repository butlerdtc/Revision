while True:
    while True:
        btype = input("What building type 'R' for Residential or 'C' for "
                      "Commercial: ").lower()
        if btype == "r" or btype == "residential":
            btype = 0.25
            break
        elif btype == "c" or btype == "commercial":
            btype = 0.5
            break
        else:
            print("Please enter valid building type")

    length = float(input("What is the length of the building(m): "))
    width = float(input("What is the width of the building(m): "))
    volume = btype * length * width
    print(f"The volume of a slab of concrete with a length of {length} and a "
          f"width of {width} with a depth of {btype} is {volume} cubic metres")
