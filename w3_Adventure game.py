# The Space Rescue Mission
# A text-based adventure game with nested if statements and three levels of choices

print("Welcome, Captain! Your ship, the Star Voyager, has received a distress signal from a nearby planet.")
print("Your mission: Rescue the stranded crew before their oxygen runs out!")

# --- Level 1 ---
choice1 = input("Do you want to LAND on the planet or ORBIT and scan first? (LAND/ORBIT): ").strip().lower()

if choice1 == "land":
    print("\nYou guide your ship through a stormy atmosphere and land near the signal source.")
    # --- Level 2 ---
    choice2 = input("You see smoke ahead. Do you INVESTIGATE the smoke, or CHECK your ship for damage first? (INVESTIGATE/CHECK): ").strip().lower()
    
    if choice2 == "investigate":
        print("\nYou find the wreckage of the stranded crew’s shuttle. The survivors wave at you for help.")
        # --- Level 3 ---
        choice3 = input("Do you APPROACH them directly, SEND a drone, or CALL them on your radio? (APPROACH/DRONE/CALL): ").strip().lower()
        
        if choice3 == "approach":
            print("\nAs you approach, alien creatures ambush you! You fight bravely but are outnumbered. Mission failed!")
        elif choice3 == "drone":
            print("\nYour drone scans the area and scares off the aliens. You rescue the survivors safely. Mission successful!")
        elif choice3 == "call":
            print("\nThey respond and warn you about nearby alien movement. You plan a safe extraction and succeed. Mission accomplished!")
        else:
            print("Your hesitation costs you precious time — the survivors’ signal fades. Mission failed.")
    
    elif choice2 == "check":
        print("\nGood thinking! You find minor hull damage and repair it quickly.")
        # --- Level 3 ---
        choice3 = input("Do you now FLY toward the signal, or WAIT for better weather? (FLY/WAIT): ").strip().lower()
        
        if choice3 == "fly":
            print("\nYou fly closer and rescue the crew just before the storm worsens. You are a hero!")
        elif choice3 == "wait":
            print("\nBy the time the storm clears, the survivors’ oxygen runs out. Mission failed.")
        else:
            print("You delay too long, and communication with the stranded crew is lost forever.")
    
    else:
        print("You stand by doing nothing, and the planet’s storm intensifies. Your ship takes fatal damage. Mission failed.")

elif choice1 == "orbit":
    print("\nYou stay in orbit and begin scanning the surface for the signal’s exact location.")
    # --- Level 2 ---
    choice2 = input("Your sensors detect two heat sources: one in the NORTH and one in the SOUTH. Where do you scan first? (NORTH/SOUTH): ").strip().lower()
    
    if choice2 == "north":
        print("\nThe northern signal shows signs of human life inside a cave.")
        # --- Level 3 ---
        choice3 = input("Do you LAND immediately, SEND a probe, or IGNORE and check the south signal? (LAND/PROBE/IGNORE): ").strip().lower()
        
        if choice3 == "land":
            print("\nYou land near the cave and find the missing crew alive. Mission successful!")
        elif choice3 == "probe":
            print("\nYour probe confirms the survivors’ location, but by the time you land, it’s too late. Mission failed.")
        elif choice3 == "ignore":
            print("\nYou switch focus to the south — but it was a trap set by pirates! They attack your ship. Mission failed.")
        else:
            print("Indecision in space can be deadly — your ship drifts into the storm and is lost.")
    
    elif choice2 == "south":
        print("\nYou detect an energy signature — possibly alien technology.")
        # --- Level 3 ---
        choice3 = input("Do you INVESTIGATE the signal, REPORT it to command, or AVOID it? (INVESTIGATE/REPORT/AVOID): ").strip().lower()
        
        if choice3 == "investigate":
            print("\nYou find advanced alien tech and use it to upgrade your ship — but forget the rescue. Mission failed.")
        elif choice3 == "report":
            print("\nCommand orders you to proceed with caution. They send reinforcements, and together you save the survivors. Mission accomplished!")
        elif choice3 == "avoid":
            print("\nYou avoid the signal and continue scanning — but find nothing else. The crew perishes. Mission failed.")
        else:
            print("You hesitate too long — your orbit decays and your ship burns up in the atmosphere.")
    
    else:
        print("Your scanners malfunction from indecision, and you lose the distress signal. Mission failed.")

else:
    print("You choose to do nothing. The distress call fades into the void. Mission failed.")
