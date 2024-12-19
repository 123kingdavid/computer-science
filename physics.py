def b():
    # speed = distance/time
   distance = float(input( " what is the distance? "))
   time = float(input(" how long was it?"))
   speed = distance*time
   print(speed)

def c():
    mass = float(input("what is the mass?"))
    acceleration  = float(input("what is acceleration?"))
    force = mass*acceleration
    print(force)



def d():
   power= float(input("what is the power?"))
   time = float(input("what is the time?"))
   energy = power*time
   print(power)


def e():
    mass  = float(input(" what is the mass?"))
    volume = float(input("what is the volume?"))
    density = mass/volume
    print(density)


def f():
    length = float(input("what is the length?"))
    breadth = float(input("what is the breadth"))
    area = length*breadth
    print(area)
def main():
        choice = input("what question do you want to perform:")

        if choice == "b":
            b()
        elif choice == "c":
            c()
        elif choice == "d":
            d()
        elif choice == "e":
            e()
        elif choice == "f":
            f()
        else:
            print('invalid input')

if __name__ == '__main__':
   main()
