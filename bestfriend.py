print("Welcome to the world of Pokemon!")
starter = input("Choose your starter! Charmander  Squirtle  Bulbasaur: ")
print(f"You choose {starter} ")
confirm = input ("Is this the Pokemon you want to start your adventure with? ")
if confirm == "Yes":
    print("Fantastic! Take these")
    print("You gained 10 Pokeballs!")
else:
    print("Choose carefully!")
    mistake = input("Choose your starter! Charmander  Squirtle  Bulbasaur: ")
    print(f"You choose {mistake} ")
confirm = input ("Is this the Pokemon you want to start your adventure with? ")
if confirm == "Yes":
    print("Fantastic! Take these")
    print("You gained 10 Pokeballs!")
    
