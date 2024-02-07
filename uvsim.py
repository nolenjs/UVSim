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
        #kicks and giggles


# Individual Methods for the Function of Each BasicML Operation
    
    #I/O Operations
    def _read(self, location): #10
        '''Reads a Word from the Keyboard and stores it in a Memory Location'''
        word = input("Enter a value: ")
        #TODO Store word at location in file
        self.counter +=1
        pass

    def _write(self, location): #11
        '''Writes a Word from a specific Memory Location to the screen.'''
        word = 0 #TODO Get word from location in file
        print(word) 
        self.counter +=1
        pass


    #Load / Store Operations
    def _load(self, location): #20
        '''Loads a word from a specific Memory Location into the Accumulator'''
        self.accumulator = 0 #TODO Get word from Location in file
        self.counter +=1
        pass

    def _store(self, location): #21
        '''Store a Word from the Accumulator into a specific Memory Location'''
        word = self.accumulator
        #TODO store word at location in file
        self.counter +=1
        pass


    #Arithmetic Operations
    def _add(self, location): #30
        '''Add the value from a specific Memory Location to the Accumulator'''
        operand = 0 #TODO Get Operand from specific Memory Location
        self.accumulator = self.accumulator + operand #Subtract the Operand Value from the Accumulator (Accumulator-Opperand) 
        self.counter += 1 #PC Increments
        pass

    def _subract(self, location): #31
        '''Subtract the value from a specific Memory Location from the Accumulator'''
        operand = 0 #TODO Get Operand from specific Memory Location
        self.accumulator = self.accumulator - operand #Subtract the Operand Value from the Accumulator (Accumulator-Opperand) 
        self.counter += 1 #PC Increments
        pass

    def _multiply(self, location): #32
        '''Multiply the Accumulator value by a value stored in a specific Memory Location'''
        operand = 0 #TODO Get Operand from specific Memory Location
        self.accumulator = self.accumulator * operand #Subtract the Operand Value from the Accumulator (Accumulator-Opperand)
        self.counter += 1 #PC Increments
        pass

    def _divide(self, location): #33
        '''Divide the Accumulator value by a value stored in a specific Memory Location'''
        operand = 0 #TODO Get Operand from specific Memory Location
        self.accumulator = self.accumulator / operand #Subtract the Operand Value from the Accumulator (Accumulator-Opperand) 
        self.counter += 1 #PC Increments
        pass


    #Control Operations
    def _branch(self, location): #40
        '''Branches Unconditionally to a specific Memory Location'''
        self.counter = location
        self.counter+=1
        pass

    def _branch_neg(self,location): #41
        '''Branches to a specific Memory Location is the Accumulator is Negative'''
        if self.accumulator < 0:
            self.counter = location
            pass
        self.counter+=1
        pass

    def _branch_zero(self,location): #42
        '''Branches to a specific Memory Location is the Accumulator is Zero'''
        if self.accumulator == 0: #Checks if Zero
            self.counter = location #Moves Counter
            pass
        self.counter+=1 #Increments Counter
        pass

    def _halt(self): #43
        '''Pauses the Program'''
        #TODO End program
        pass
