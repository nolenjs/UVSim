class UVSim:
    def __init__(self, counter = 0, accumulator = 0):
        self.counter = counter
        self.accumulator = accumulator
        with open("program.txt", "r") as f:
            self.program = f.readlines()
            for p in range(0,len(self.program)):
                self.program[p] = self.program[p].strip() #Remove any whitespace characters

    #Other functions to come, but something to get started
        #kicks and giggles
                
    def get_accumulator(self):
        return self.accumulator
    
    def get_counter(self):
        return self.counter

    def _check_location(self,location): #Checks if the location in memory is valid
        if location >=0 and location < len(self.program):
            return location
        else:
            raise IndexError("Location Index out of range")
           

# Individual Methods for the Function of Each BasicML Operation
    
    #I/O Operations
    def _read(self, location): #10
        '''Reads a Word from the Keyboard and stores it in a Memory Location'''
        print(f"Read From Keyboard to: {location}") #Shout for Testing
        self._check_location(location)
        while True:
            word = input("Enter a value as form of a word (4 digits with an optional negative sign in front): ")
            if len(word) == 5 and word[0] == '-':
                if word[1:].isdigit():
                    break

            if len(word) == 4:
                if word.isdigit():
                    break

        self.program[location] = str(word) #Store word at location in file
        self.counter +=1
        return word
    
    def _write(self, location): #11
        '''Writes a Word from a specific Memory Location to the screen.'''
        print(f"Print From {location} to Screen") #Shout for Testing
        self._check_location(location)
        word = self.program[location] #Get word from location in file
        print(word) 
        self.counter +=1
        return word


    #Load / Store Operations
    def _load(self, location): #20
        '''Loads a word from a specific Memory Location into the Accumulator'''
        self._check_location(location)
        self.accumulator = int(self.program[location])
        self.counter += 1
        

    # def _store(self, location): #21
    #     '''Store a Word from the Accumulator into a specific Memory Location'''
    #     print(f"Store From Accumulator to {location}") #Shout for Testing
    #     self._check_location(location)
    #     word = self.accumulator
    #     self.program[location] = str(word) #store word at location in file
    #     self.counter +=1
        
    def _store(self, location): #21
        '''Store a Word from the Accumulator into a specific Memory Location'''        
        self._check_location(location)
        temp = "" # To fill the 4-digit requirement of a word
        if self.accumulator < 0:
            temp = "-" + temp
            self.accumulator = self.accumulator * -1
        if self.accumulator < 1000 and self.accumulator > -1000:
            temp += "0"
            if self.accumulator < 100 and self.accumulator > -100:
                temp += "0"
                if self.accumulator < 10 and self.accumulator > -10:
                    temp += "0"
        
        self.program[location] = temp + str(self.accumulator)
        self.counter += 1


    #Arithmetic Operations
    def _add(self, location): #30
        '''Add the value from a specific Memory Location to the Accumulator'''
        print(f"Add from {location} to Accumulator") #Shout for Testing
        self._check_location(location)
        operand = self.program[location] #Get Operand from specific Memory Location
        operand = int(operand)
        self.accumulator = self.accumulator + operand #Subtract the Operand Value from the Accumulator (Accumulator-Opperand) 
        self.counter += 1 #PC Increments
        

    def _subtract(self, location): #31
        '''Subtract the value from a specific Memory Location from the Accumulator'''
        print(f"Subtract from {location} from Accumulator") #Shout for Testing
        self._check_location(location)
        operand = self.program[location] #Get Operand from specific Memory Location
        operand = int(operand)
        self.accumulator = self.accumulator - operand #Subtract the Operand Value from the Accumulator (Accumulator-Opperand) 
        self.counter += 1 #PC Increments
        

    def _multiply(self, location): #32
        '''Multiply the Accumulator value by a value stored in a specific Memory Location'''
        print(f"Multipy from {location} by Accumulator") #Shout for Testing
        self._check_location(location)
        operand = self.program[location] #Get Operand from specific Memory Location
        operand = int(operand)
        self.accumulator = self.accumulator * operand #Subtract the Operand Value from the Accumulator (Accumulator-Opperand)
        self.counter += 1 #PC Increments
        

    def _divide(self, location): #33
        '''Divide the Accumulator value by a value stored in a specific Memory Location'''
        print(f"Divide from {location} by Accumulator") #Shout for Testing
        self._check_location(location)
        operand = self.program[location] #Get Operand from specific Memory Location
        operand = int(operand)
        if operand == 0:
            raise ValueError("Divide by Zero")
        self.accumulator = int((self.accumulator / operand) + 0.5) #Round the result & turn into an int
        # self.counter += 1 #PC Increments
        self.counter += 1
        


    #Control Operations
    def _branch(self, location): #40
        '''Branches Unconditionally to a specific Memory Location'''
        print(f"Branch to {location}") #Shout for Testing
        self._check_location(location)
        self.counter = location

    def _branch_neg(self,location): #41
        '''Branches to a specific Memory Location is the Accumulator is Negative'''
        print(f"Branch to {location} if Neg") #Shout for Testing
        self._check_location(location)
        if self.accumulator < 0:
            self.counter = location
            

    def _branch_zero(self,location): #42
        '''Branches to a specific Memory Location is the Accumulator is Zero'''
        print(f"Branch to {location} if Zero") #Shout for Testing
        self._check_location(location)
        if self.accumulator == 0: #Checks if Zero
            self.counter = location #Moves Counter
            

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

            # Validates the Input

            #If that line is empty
            if len(current) == 0:
                while len(current) == 0:
                    self.counter += 1
                    current = self.program[self.counter]

            elif len(current) != 4 and (len(current) != 5 and current[0] == "-") or not current.isdigit():
                raise SyntaxError("Invalid Operation")

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
                self._subtract(operand) #SUB
            elif opcode == 32:
                self._multiply(operand) #MUL
            elif opcode == 33:
                self._divide(operand) #DIV

            elif opcode == 40:
                self._branch(operand) #BRANCH
                self.counter += 1
            elif opcode == 41:
                self._branch_neg(operand) #BRANCHNEG
                self.counter += 1
            elif opcode == 42:
                self._branch_zero(operand) #BRANCHZERO
                self.counter += 1

            elif opcode == 43:
                #HALT
                self._halt()
                run_program = False
                return True
            
            elif opcode == 0: #No Op
                print("NoOp")
                self.counter +=1
            else:
                raise SyntaxError("Invalid Operation")

            #run_program = False #Escape for Testing
        return False


