class UVSim:
    def __init__(self, counter = 0, accumulator = 0):
        self.counter = counter
        self.accumulator = accumulator
        with open("../program.txt", "r") as f:
            self.program = f.readlines()
            for p in range(0,len(self.program)):
                self.program[p] = self.program[p].strip() #Remove any whitespace characters

    def _check_location(self,location): #Checks if the location in memory is valid
        if location >=0 or location < len(self.program):
            pass
        else:
            raise IndexError("Location Index out of range")
        pass   
# Individual Methods for the Function of Each BasicML Operation
    
    #I/O Operations
    def _read(self, location): #10
        '''Reads a Word from the Keyboard and stores it in a Memory Location'''
        print(f"Read From Keyboard to: {location}") #Shout for Testing
        self._check_location(location)
        word = input("Enter a value: ")
        self.program[location] = int(word) #Store word at location in file
        pass

    def _write(self, location): #11
        '''Writes a Word from a specific Memory Location to the screen.'''
        print(f"Print From {location} to Screen") #Shout for Testing
        self._check_location(location)
        word = self.program[location] #Get word from location in file
        print(word)  
        pass


    #Load / Store Operations
    def _load(self, location): #20
        '''Loads a word from a specific Memory Location into the Accumulator'''
        self._check_location(location)
        self.accumulator = int(self.program[location])
        pass

    def _store(self, location): #21
        '''Store a Word from the Accumulator into a specific Memory Location'''        
        self._check_location(location)
        temp = "" # To fill the 4-digit requirement of a word
        if self.accumulator < 1000 and self.accumulator > -1000:
            temp += "0"
            if self.accumulator < 100 and self.accumulator > -100:
                temp += "0"
        if self.accumulator < 0:
            temp = "-" + temp
        self.program[location] = temp + str(self.accumulator)
        pass


    #Arithmetic Operations
    def _add(self, location): #30
        '''Add the value from a specific Memory Location to the Accumulator'''
        print(f"Add from {location} to Accumulator") #Shout for Testing
        self._check_location(location)
        operand = self.program[location] #Get Operand from specific Memory Location
        self.accumulator = self.accumulator + operand #Subtract the Operand Value from the Accumulator (Accumulator-Opperand) 
        pass

    def _subract(self, location): #31
        '''Subtract the value from a specific Memory Location from the Accumulator'''
        print(f"Subtract from {location} from Accumulator") #Shout for Testing
        self._check_location(location)
        operand = self.program[location] #Get Operand from specific Memory Location
        self.accumulator = self.accumulator - operand #Subtract the Operand Value from the Accumulator (Accumulator-Opperand) 
        pass

    def _multiply(self, location): #32
        '''Multiply the Accumulator value by a value stored in a specific Memory Location'''
        print(f"Multipy from {location} by Accumulator") #Shout for Testing
        self._check_location(location)
        operand = self.program[location] #Get Operand from specific Memory Location
        self.accumulator = self.accumulator * operand #Subtract the Operand Value from the Accumulator (Accumulator-Opperand)
        pass

    def _divide(self, location): #33
        '''Divide the Accumulator value by a value stored in a specific Memory Location'''
        print(f"Divide from {location} by Accumulator") #Shout for Testing
        self._check_location(location)
        operand = self.program[location] #Get Operand from specific Memory Location
        if operand == 0:
            raise ValueError("Divide by Zero")
        self.accumulator = int((self.accumulator / operand) + 0.5) #Round the result & turn into an int
        pass


    #Control Operations
    def _branch(self, location): #40
        '''Branches Unconditionally to a specific Memory Location'''
        print(f"Branch to {location}") #Shout for Testing
        self._check_location(location)
        self.counter = location
        self.counter -= 1
        pass

    def _branch_neg(self,location): #41
        '''Branches to a specific Memory Location is the Accumulator is Negative'''
        print(f"Branch to {location} if Neg") #Shout for Testing
        self._check_location(location)
        if self.accumulator < 0:
            self.counter = location
            self.counter -= 1
            pass
        pass

    def _branch_zero(self,location): #42
        '''Branches to a specific Memory Location is the Accumulator is Zero'''
        print(f"Branch to {location} if Zero") #Shout for Testing
        self._check_location(location)
        if self.accumulator == 0: #Checks if Zero
            self.counter = location #Moves Counter
            self.counter -= 1
            pass
        pass

def run(self): #Runs program until Halt
        self.counter = 0 #Reset Counter
        self.accumulator = 0 #Reset Accumulator
        while self.counter < len(self.program):
            #Get Next Line
            current = self.program[self.counter] #Start at current PC position

            #If that line is empty
            if len(current) == 0:
                while len(current) == 0:
                    self.counter += 1
                    current = self.program[self.counter]

            #Exract opcode
            if current[0] == "-":
                opcode = int(str(current)[:3]) #Get first three digits
            else:
                opcode = int(str(current)[:2]) #Get first two digits
            operand= int(current) % 100 #GeT Last Two Digits
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

            elif opcode == 43: #HALT
                print(f"Halt the Program") #Shout for Testing
                break
            
            elif opcode == 0: #No Op
                print("NoOp")
            else:
                raise SyntaxError("Invalid Operation")
            
            self.counter += 1 #PC Increments
            #run_program = False #Escape for Testing
        return 0


def main(): #The Console interface for the Program
    sim = UVSim(0,0) #Create a UVSim object for the user to use in the console appliaction
    sim.run() #Run Sim

if __name__ == "__main__":
    main()
