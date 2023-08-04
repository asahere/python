class convert:
    def __init__(self,num):
        self.num=num
    def to_roman(self):
        if self.num==1:
            return "I"
        elif self.num==2:
            return "II"
        elif self.num==3:
            return "III"
        elif self.num==4:
            return "IV"
        elif self.num==5:
            return "V"
        elif self.num==6:
            return "VI"
        elif self.num==7:
            return "VII"
        elif self.num==8:
            return "VIII"
        elif self.num==9:
            return "IX"
        elif self.num==10:
            return "X"
        else:
            print("Wrong input!!!")

    def to_int(self,rom):
        self.rom=rom
        if self.rom=="I":
            return 1
        elif self.rom=="II":
            return 2
        elif self.rom=="III":
            return 3
        elif self.rom=="IV":
            return 4
        elif self.rom=="V":
            return 5
        elif self.rom=="VI":
            return 6
        elif self.rom=="VII":
            return 7
        elif self.rom=="VIII":
            return 8
        elif self.rom=="IX":
            return 9
        elif self.rom=="X":
            return 10
        else:
            print("Wrong input!!!")

print("Enter the the choice y")

con1=convert()
n=int(input("Enter a number:"))
rnum=con1.int_to_roman(n)
print(n,"in roman number is:",rnum)
                
            


        

