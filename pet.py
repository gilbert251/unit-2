class pet:    
    def __init__(self,name,species):
     self.name = name
     self.species = species
     self.hunger = 50      
     self.happiness = 50   
     self.energy = 100  

    def feed(self):
       self.hunger=min(100, self.hunger + 50)
       self.energy=min(100, self.energy + 50)
       
    def play(self):
       self.happiness += 20
       self.energy -= 20
       self.hunger -= 20

    def check_status(self):    
            if self.hunger < 0:
                print("your pet is hungry")
            if self.energy < 0:
                print("your pet is tired")
            if self.happiness < 0:
               print("your pet is bored")
    def time_passes(self):
        self.hunger = max(0, self.hunger - 10)
        self.happiness = max(0, self.happiness - 5)
        self.energy = max(0, self.energy - 5)


name = input("what do you want to name your pet?")
species = input("what type of pet do you want?")
my_pet = pet(name, species)

print(f"\nSuccess! You created {my_pet.name} the {my_pet.species}.")
playing=1
while playing:
 print(f"Stats -> Hunger: {my_pet.hunger}, Happiness: {my_pet.happiness}, Energy: {my_pet.energy}")
 print("what do you want to do?: play,feed,check status,exit")
 user_input=input()
 if user_input=="play":
    my_pet.play()
 elif user_input=="feed":
    my_pet.feed()
 elif user_input=="check status":
    my_pet.check_status()
 elif user_input=="exit":
    print("thanks for playing")
    break
 else:print("invalid choice")
 print(f"Stats -> Hunger: {my_pet.hunger}, Happiness: {my_pet.happiness}, Energy: {my_pet.energy}")
 my_pet.time_passes()
