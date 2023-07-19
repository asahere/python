def shape_name(num_sides,side_lengths):
    if num_sides==3:
        if side_lengths[0]==side_lengths[1]==side_lengths[2]:
            print("equilateral Triangle")
        elif side_lengths[0]==side_lengths[1]!=side_lengths[2]
            print("Isolateral Triangle")
        else:
            print("Triangle")
    elif num_sides==4:
        if side_lengths[0]==side_lengths[1]==side_lengths[2]==side_lengths[3]:
            print("Square")
        elif side_lengths[0]==side_lengths[2] and side_lengths[1]==side_lengths[3]:
            print("Rectangle")
        elif side_lengths[0==side_lengths[2]] and side_lengths[1]!=side_lengths[3]:
            print("Rhombus")
        else:
            print("Quadrilateral")
    elif num_sides==5:
        print("Pentagon")
    elif num_sides==6:
        print("Hexagon")
    elif num_sides==7:
        print("Heptagon")
    elif num_sides==8:
        print("Octagon")
    elif num_sides==9:
        print("Nonagon")
    elif num_sides==10:
        print("Decagon")
    else:
        print("Unknown Shape")

def main():
    num_sides=int(input("Enter the number of sides:"))
    if num_sides<=2:
        print("A shape must have at least 3 sides")
    else:
        side_lengths=[]
        for i in range(num_sides):
            side_length=int(input(f"En"))