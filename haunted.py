# Final Challenge!
# Expand the haunted house. You might add another door, or create more rooms beyond the existing ones. You might also use a "while loop" to keep you longer in certain rooms, and add more options for responding to the prompt for those rooms.

while True:
    print("You come upon a dark house with two doors")
    print("Do you go through door #1 or door #2?")

    door = input("> ")

    if door == "1":
        print("There's a monster coming up from the ground!")
        print("What do you do?")
        print("1. Kick him on the head.")
        print("2. Run away.")

        monster = input("> ")

        if monster == "1":
            print("Big mistake! He grabs your foot and eats you alive.")
        elif monster == "2":
            print("You're too slow... he chases you down and eats you alive!")
        else:
            print(f"Well, {monster} is probably the better option.")
            print("Monster runs away.")

    elif door == "2":
        print("In the first room, you see two more doors, one made of iron and one made of wood")
        print("1. Go in the iron door")
        print("2. Go in the wooden door")
        print("3. Stay right where you are")

        choice = input("> ")

        if choice == "1":
            print("You come across a chest filled with golden treasure.")
            print("Good job!")
            break
        elif choice == "2":
            print("You step into a trapdoor and fall...")
            print("...forever.")
        elif choice == "3":
            print("After hanging out for a while, you notice a little mouse drowning in a puddle. What do you do?")
            print("1. Pick it up")
            print("2. Ignore it and move on to the next room.")
            
            mouse = input("> ")

            if mouse == "1":
                print("Wow! It turns into a magical fairy princess. She will grant you one wish. What is it?")
                wish = input("> ")
                print(f"{wish} sounds like a very nice wish.")
                print("Your wish has been granted.")
                break
            elif mouse == "2":
                print("Wow! The mouse turns into a terrible monster who grabs your foot at eats you.")
                print("Well done.")
            else:
                print("You should run away now while you have the chance!")
        else:
            print("You're idling has awoken the angry spirits of the house")
            print("Run away!")

    else:
        print("You wait to long and the monster from room #1 breaks through the door and eats you!")
