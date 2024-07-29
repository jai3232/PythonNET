def make_coffee(*flavors):
    """
    This function takes an arbitrary number of coffe floavors and prints them
    """
    print("I am a barista. Making the followintg coffees: ")
    for flavor in flavors:
        print(f"flavor {flavor}")