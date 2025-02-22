# Mohammad Javad, who has great perseverance, was a simple plumber at first (of course, now he has gone through all the
# steps of promotion with his perseverance). He had to know at any moment what the condition of the water inside the samovar
# is. Therefore, he attached a thermometer to the samovar and should measure the water condition according to the temperature
# of the water inside the samovar. We know that at normal pressure, water is vapor at a temperature of more than 100 degrees and
# freezes at a temperature of less than 0. (The water inside the samovar may freeze in winter) Now you know that you have to work
# hard to succeed. That's why sooner or later you have to decide to follow Mohammad Javad's path. For this, you need to determine
# the state of water (actually H2OH2O) inside the samovar according to the temperature inside the samovar.
# input
# In the first line of the input, there is an integer number TT, which indicates the temperature of the water inside the samovar.
# −273<T≤6000
# output
# If the temperature inside the samovar is more than 100 degrees, Steam will be printed. If its temperature was below 0, Ice will
# be printed and otherwise, Water will be printed.

T = int(input())
if -273 < T <= 6000:
    if T>100:
        print("Steam")
    elif T<0 :
        print("Ice")
    else:
        print("Water")
else :
    print("your num should be between -273 and 6000 ")