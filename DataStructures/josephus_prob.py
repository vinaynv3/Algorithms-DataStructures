

"""
Josephus problem is 1st century story that in jewish revolt againt Rome.

"""

from queue import Queue

def spin(alist,marker):

    circle = Queue()

    for student in alist:
        circle.add(student)

    while len(circle) > 1:

        for round in range(marker):
            circle.add(circle.remove())

        circle.remove()
    
    return circle[0]

def main():

    alist = ["Bill","David","Susan","Jane","Kent","Brad"]
    print(spin(alist,7))

if __name__ == "__main__":
    main()



