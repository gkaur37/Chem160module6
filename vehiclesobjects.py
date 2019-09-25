def vehicle(x,y,z):
    return x,y,z
car1=vehicle(4,4,"sedan")
car2=vehicle(2,4,"coupe")
car3=vehicle(2,4,"mini")
cycle=vehicle(0,2,"motorcycle")
truck=vehicle(18,2,"semi")
car1
print(car1)
car1==car2
car2==car3
car1+=cycle
print(car1)
