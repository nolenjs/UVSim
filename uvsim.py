class UVSim:
    def __init__(self, counter, accumulator):
        self.counter = 0
        self.accumulator = 0
        with open("./program.txt", "r") as f:
            self.program = f.readlines()
            for p in self.program:
                p = p.strip() #Remove any whitespace characters

    def write(self, index):
        print("Save the accumulator's value to the file", self.accumulator)

    def read(self, index):
        print("Save the line's value to the accumulator", self.accumulator)

    #Other functions to come, but something to get started