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
        print(f"Read From Keyboard to: {location}") #Shout for Testing
        word = input("Enter a value: ")
        self.program[location] = int(word) #Store word at location in file
        self.counter +=1
        pass

    def _write(self, location): #11
        '''Writes a Word from a specific Memory Location to the screen.'''
        print(f"Print From {location} to Screen") #Shout for Testing
        word = self.program[location] #Get word from location in file
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
        print(f"Store From Accumulator to {location}") #Shout for Testing
        word = self.accumulator
        self.program[location] = word #store word at location in file
        self.counter +=1
        pass


    #Arithmetic Operations
    def _add(self, location): #30
        '''Add the value from a specific Memory Location to the Accumulator'''
        print(f"Add from {location} to Accumulator") #Shout for Testing
        operand = self.program[location] #Get Operand from specific Memory Location
        self.accumulator = self.accumulator + operand #Subtract the Operand Value from the Accumulator (Accumulator-Opperand) 
        self.counter += 1 #PC Increments
        pass

    def _subract(self, location): #31
        '''Subtract the value from a specific Memory Location from the Accumulator'''
        print(f"Subtract from {location} from Accumulator") #Shout for Testing
        operand = self.program[location] #Get Operand from specific Memory Location
        self.accumulator = self.accumulator - operand #Subtract the Operand Value from the Accumulator (Accumulator-Opperand) 
        self.counter += 1 #PC Increments
        pass

    def _multiply(self, location): #32
        '''Multiply the Accumulator value by a value stored in a specific Memory Location'''
        print(f"Multipy from {location} by Accumulator") #Shout for Testing
        operand = self.program[location] #Get Operand from specific Memory Location
        self.accumulator = self.accumulator * operand #Subtract the Operand Value from the Accumulator (Accumulator-Opperand)
        self.counter += 1 #PC Increments
        pass

    def _divide(self, location): #33
        '''Divide the Accumulator value by a value stored in a specific Memory Location'''
        print(f"Divide from {location} by Accumulator") #Shout for Testing
        operand = self.program[location] #Get Operand from specific Memory Location
        self.accumulator = self.accumulator / operand #Subtract the Operand Value from the Accumulator (Accumulator-Opperand) 
        self.counter += 1 #PC Increments
        pass


    #Control Operations
    def _branch(self, location): #40
        '''Branches Unconditionally to a specific Memory Location'''
        print(f"Branch to {location}") #Shout for Testing
        self.counter = location
        pass

    def _branch_neg(self,location): #41
        '''Branches to a specific Memory Location is the Accumulator is Negative'''
        print(f"Branch to {location} if Neg") #Shout for Testing
        if self.accumulator < 0:
            self.counter = location
            pass
        self.counter+=1
        pass

    def _branch_zero(self,location): #42
        '''Branches to a specific Memory Location is the Accumulator is Zero'''
        print(f"Branch to {location} if Zero") #Shout for Testing
        if self.accumulator == 0: #Checks if Zero
            self.counter = location #Moves Counter
            pass
        self.counter+=1 #Increments Counter
        pass

    def _halt(self): #43
        '''Pauses the Program'''
        print(f"Halt the Program") #Shout for Testing
        #End program Handled By run Method
        pass



def run(self): #Runs program until Halt
        self.counter = 0 #Reset Counter
        self.accumulator = 0 #Reset Accumulator
        run_program = True
        while run_program:
            #Get Next Line
            current = self.program[self.counter] #Start at current PC position

            #Exract opcode
            opcode = int(str(current)[:2]) #Get first two digits
            operand= current % 100 #GeT Last Two Digits
            print(f"OpCode: {opcode} Operand: {operand}")

            #Run Operation

            if opcode == 10:
                self._read(operand) #READ
            elif opcode == 11:
                self._write(operand) #WRITE

            elif opcode == 20:
                self._load(operand) #LOAD
            elif opcode == 21:
                self._store(operand) #STORE

            elif opcode == 30:
                self._add(operand) #ADD
            elif opcode == 31:
                self._subract(operand) #SUB
            elif opcode == 32:
                self._multiply(operand) #MUL
            elif opcode == 33:
                self._divide(operand) #DIV

            elif opcode == 40:
                self._branch(operand) #BRANCH
            elif opcode == 41:
                self._branch_neg(operand) #BRANCHNEG
            elif opcode == 42:
                self._branch_zero(operand) #BRANCHZERO

            elif opcode == 43:
                #HALT
                self._halt()
                run_program = False
            
            elif opcode == 0: #No Op
                print("NoOp")
                self.counter +=1
            else:
                print("Invalid Operation")

            #run_program = False #Escape for Testing
        return 0


def main(): #The Console interface for the Program
    sim = UVSim(0,0) #Create a UVSim object for the user to use in the console appliaction
    sim.run() #Run Sim

if __name__ == "__main__":
    main()
