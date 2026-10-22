def gamble(quarters, play_A, play_B,play_C,play_total):
 
 play_total=0

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


play_total = gamble(25)
print(f"Martha plays {play_total} times before going broke.")
