num_beers = 99
def song(num_beers):
    while num_beers > 0:
        if num_beers == 1:
            print(num_beers)
            print(" bottle of beer on the wall,"),
            print(num_beers),
            print(" bottle of beer.")
            print("if one of those bottles should happen to fall,"),
            print(" One less bottle of beer on the wall.\n")
        else:
            print(num_beers),
            print(" bottles of beer on the wall,"),
            print(num_beers),
            print(" bottles of beer.")
            print("if one of those bottles should happen to fall,")
            num_beers-=1
            if num_beers > 1:
                print(num_beers),
                print(" bottles of beer on the wall.\n")

song(num_beers)



    
