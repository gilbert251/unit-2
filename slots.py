def gamble(quarters, play_A=0, play_B=0, play_C=0,play_total=0):

 while(0<quarters):
    play_A += 1
    quarters -= 1
    play_total += 1
    if quarters == 0:
        return play_total
    if play_A == 35:
      quarters += 30
      play_A = 0
    play_B += 1 
    quarters -= 1
    play_total += 1
    if quarters == 0:
       return play_total
    if play_B == 100:
       quarters += 60
       play_B = 0
    play_C += 1
    quarters -= 1
    play_total += 1
    if quarters == 0: 
       return play_total
    if play_C == 10:
       quarters += 9
       play_C = 0


user_input = int(input("Enter starting quarters: "))
start_A = int(input("Enter times Machine A has been played: "))
start_B = int(input("Enter times Machine B has been played: "))
start_C = int(input("Enter times Machine C has been played: "))
if user_input < 0:
    print("Please enter a positive number.")
else:
    play_total = gamble(user_input)
    print(f"Martha plays {play_total} times before going broke.")
