import math

def getDelta(a,b,c):
    d = (b**2) - (4*a*c)
    return d

def main():
    a = float(input("Give the value of a : "))
    b = float(input("Give the value of b : "))
    c = float(input("Give the value of c : "))
    d = getDelta(a,b,c)
    print("Your delta is equal to : " + str(d))
    if a == 0:
        r = -c / b
        print("r = {}".format(r))
    else:    
        if d > 0:
            r1 = (-b + math.sqrt(d)) / (2*a)
            r2 = (-b - math.sqrt(d)) / (2*a)
            print("r1 = {} and r2 = {}".format(r1, r2))
        elif d == 0:
            r = (-b + math.sqrt(d)) / (2*a)
            print("r = {}".format(r))
        else:
            square_delta = complex(0, math.sqrt(-d))
            r1 = (-b + square_delta) / (2*a)
            r2 = (-b - square_delta) / (2*a)
            print("r1 = {} and r2 = {}".format(r1, r2))
            
main()