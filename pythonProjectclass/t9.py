distance=int(input("enter distance between two city: "))
avrage_speed=int(input("enter avrage_speed : "))
benzin=int(input("enter how much benzin used per 100km : "))
cost_of_benzin=int(input("enter cost of benzin : "))
time=distance/avrage_speed
gas=distance/100*benzin #mizan masrafe benzin
cost=gas*cost_of_benzin
print("time you need for travil is:", time)
print("you need",gas,"gas for ur trip")
print("you have to pay",cost,"for this trip")
#also you can do it for print
print(f"time:{time}, gas:{gas}, cost:{cost}")
