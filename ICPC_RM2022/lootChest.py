# Loot Chest
# iL = probability increase when you loose a match
# iW = probability increase when you win a match and failed to receive a prize
# G = chance of getting gorilla
# L = chance of loosing each match
# P = probability of getting prize

"""
You start with P = 0. You have an L% chance of loosing each match you play.
Given iL, iW, G and L, compute the expected number of matches you will have to play
to win the gorilla prize.


    w = (4-100*(3855.939044/15643)-50*(-2/5)) 
    x = (3855.939044/15643)
    y = -(2/5)
    z = (4950*(3855.939044/15643)-1157.16667)/25
    m = (iL*w) + (iW*x) + (G*y) + (L*z)

"""
i = input().split()

P = 0

iL = int(i[0])
iW = int(i[1])
G = int(i[2])
L = int(i[3])
 
P = min(P+iW, 100)





print(matches_to_play(iL, iW, G, L))