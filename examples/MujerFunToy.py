#Mujer Fun toy app to make Fun toys for mujers
#Created by Chace
class Toy:
    """
    Toy class to characterize a Fun Toy.
    """

    def __init__(self, size, color, vibrations):
        """
        This is the initialize function. In here the object gets initialized when it is called into the scope with these
        values and it must be initialized with the parameters size, color, and leaves.

        :param size: The size of the plant (small, med, large)
        :param color: Color of the plant
        :param leaves: If the plant has leaves or not (True or False)
        """
        self.size = size
        self.color = color
        self.vibrations = vibrations
        self.height = 0

    def grow(self, growth):
        """
        This function is a method that acts on the data of the plant class. It makes the toy grow!

        :param growth: The amount the plant should grow by
        """

        self.height = growth

    def colorchange(self, colorchange):
        self.color = colorchange

    def stretch(self, sizechange):
        self.size = sizechange

    def vibrationstoggle(self, vibration):
        self.vibrations = bool(vibration)

# To initialize an object you have to call it by setting it to a variable and calling it like so

thestandardtoy = Toy("medium", "pink", True)

print ("Welcome to Mujer Toy Builder")
thestandardtoy.size = input("What girth would you like your toy? (Small, Medium, Or Large)")
thestandardtoy.color = input("What color would you like your toy? (Pink, White, Black, ETC)")
thestandardtoy.vibrations = input("Do you want it to vibrate? (True or False)").upper()
thestandardtoy.height = input("How many inches do you want your toy to be")


exit == False
while(exit != True):
    print("Congrats, your toy has been created")
    print(thestandardtoy.color + " " + thestandardtoy.height + " Inch " + thestandardtoy.size + " Girthed Mujer Custom TOY")
    if (thestandardtoy.vibrations == "TRUE"):
        print("THAT VIBRATES!")
    change = input("Do you want to change the anything? (Size, Color, Vibrations, Height)\n Type No to Stop EDITS\n").upper()
    if change == "HEIGHT":
        change = input("Enter new height")
        thestandardtoy.grow(change)
    elif change == "SIZE":
        change = input("Enter new size (Small, Medium, Or Large)")
        thestandardtoy.stretch(change)

    elif change == "COLOR":
        change = input("Enter New color (Gold, Green, Purple, ETC)")
        thestandardtoy.colorchange(change)

    elif change == "VIBRATIONS":
        change = input("Vibrations? (True or False)").upper()
        thestandardtoy.vibrationstoggle(change)

    elif change == "NO":
        exit = True


print("Congrats, your toy has been created")
print(thestandardtoy.color + " " + thestandardtoy.height + " Inch " + thestandardtoy.size + " Girthed Mujer Custom TOY")


print("Enjoy")