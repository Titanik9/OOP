class Computer:
    def __init__(self, ram, processor, memory):
        self.ram = ram
        self.processor = processor
        self.memory = memory

    def getspecs(self):
        self.ram = input("Enter ram size")
        self.processor = input("Enter type of processor")
        self.memory = input("Enter memory size")

    def displayspecs(self):
        print(f"Ram:" + self.ram + "and Type of processor:" + self.processor + "and Memory size:" + self.memory)

class Laptop(Computer):
    def __init__(self, color):
        self.color = color

    def getcolor(self):
        self.color = input("Enter color")

    def displaycolor(self):
        print("Color of laptop: " + self.color)

class Desktop(Computer):
    def specification(self, weight):
        self.weight = weight

comp = Laptop('')
comp.getspecs()
comp.displayspecs()
comp.getcolor()
comp.displaycolor()
