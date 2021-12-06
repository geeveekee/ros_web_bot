from math import sqrt, atan
from icecream import ic

a1 = 4.32
a2 = 5.105
r = 1

x = 0.01
z = -0.5

    
polarRadius = sqrt(x*x + z*z )
angle = atan(z/x)
ic(angle)

#2nd quadrant
if (x < 0 and z > 0):
    a1 = -(3.14 - a1)
    a2 = a2
    ic(a1, a2)
    if((angle > a1) and (angle < a2)):
        ic(a1, a2)
        print("Inside")
    else:
        print("outside")

#3rd quadrant
elif (x < 0 and z < 0):
    a1 = -(3.14 - a1)
    a2 = -(3.14 - a2)
    ic(a1, a2)
    if((angle > a1) and (angle < a2)):
        ic(a1, a2)
        print("Inside")
    else:
        print("outside")

#4th quadrant
elif (x > 0 and z < 0):
    a1 = a1
    a2 = -(a2 - 3.14)
    ic(a1, a2)
    if((angle > a1) and (angle < a2)):
        ic(a1, a2)
        print("Inside")
    else:
        print("outside")

#gg
else:
    a1 = a1
    a2 = a2
    ic(a1, a2)
    if((angle > a1) and (angle < a2)):
        ic(a1, a2)
        print("Inside")
    else:
        print("outside")
