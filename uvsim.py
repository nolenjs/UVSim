import os

class UVSim:
    def __init__(self, counter = 0, accumulator = 0):
        self.counter = counter
        self.accumulator = accumulator
        self.pause = False

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

    def _check_location(self,location): #Checks if the location in memory is valid
        if location >=0 or location < len(self.program):
            pass
        else:
            raise IndexError("Location Index out of range")
# Individual Methods for the Function of Each BasicML Operation
    
    #I/O Operations
    def _read(self, location): #10
        '''Reads a Word from the Keyboard and stores it in a Memory Location'''
        print(f"Read From Keyboard to: {location}") #Shout for Testing
        self._check_location(location)
        condition = False
            
        with open("output.txt", "a") as file_out:       # Prompt User for Input: 
            file_out.write("Enter a value as form of a word (4 digits with an optional negative sign in front):|")
            
        if os.path.getsize("input.txt") > 0:            # If Input file changes or in other words, if input is entered
            with open("input.txt","r") as file_in:
                word = file_in.read()
                if len(word) == 5 and word[0] == '-':
                    if word[1:].isdigit():
                        condition = True

                elif len(word) == 4:
                    if word.isdigit():
                        condition = True

                else: 
                    raise TypeError("Invalid Type")  
            
                if condition == True:
                    self.program[location] = str(word) #Store word at location in file
                    self.counter +=1
                    return word

        
    
    def _write(self, location): #11
        '''Writes a Word from a specific Memory Location to the screen.'''
        print(f"Print From {location} to Screen") #Shout for Testing
        self._check_location(location)
        word = self.program[location] #Get word from location in file
        # print(word)
        with open("output.txt","a") as file_out:
            file_out.write(f"{word}") 
        self.counter +=1
        return word

    #Load / Store Operations
    def _load(self, location): #20
        '''Loads a word from a specific Memory Location into the Accumulator'''
        self._check_location(location)
        self.accumulator = int(self.program[location])
        self.counter += 1

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
    def _arithmetic(self, code, location): #30
        '''Add the value from a specific Memory Location to the Accumulator'''
        print(f"Add from {location} to Accumulator") #Shout for Testing
        self._check_location(location)
        operand = self.program[location] #Get Operand from specific Memory Location
        operand = int(operand)
        if code == 30 or code == 31:
            if code == 31:
                operand *= -1 #Subtraction = Negative Addition
            self.accumulator = self.accumulator + operand #Add the Operand Value from the Accumulator (Accumulator+Opperand) 
        if code == 32:
            self.accumulator = self.accumulator * operand
        if code == 33:
            if operand == 0:
                raise ValueError("Divide by Zero")
            self.accumulator = int((self.accumulator / operand) + 0.5) #Round the result & turn into an int
        self.counter += 1 #PC Increments

    #Control Operations
    def _branch(self, code, location): #40
        '''Branches Unconditionally to a specific Memory Location'''
        print(f"Branch to {location}") #Shout for Testing
        self._check_location(location)
        if code == 40:
            self.counter = location
        elif self.accumulator < 0 and code == 41:
            self.counter = location
        elif self.accumulator == 0 and code == 42: #Checks if Zero
            self.counter = location #Moves Counter
            

    def _halt(self): #43
        '''Pauses the Program'''
        print(f"Halt the Program") #Shout for Testing
        #End program Handled By run Method
        pass

    def run(self): #Runs program until Halt
        with open("input.txt","w") as f:
            pass
        with open("output.txt","w") as f:
            pass

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
            if not self.pause:
                if opcode == 10:
                    self._read(operand) #READ
                    with open("input.txt","w") as f:
                        pass
                    
                elif opcode == 11:
                    self._write(operand) #WRITE

                elif opcode == 20:
                    self._load(operand) #LOAD
                elif opcode == 21:
                    self._store(operand) #STORE

                elif opcode >= 30 and opcode <= 33:
                    self._arithmetic(opcode, operand) #ADD

                elif opcode <= 40 and opcode >= 42:
                    self._branch(opcode, operand) #BRANCH
                    self.counter += 1

                elif opcode == 43:
                    #HALT
                    self._halt()
                    run_program = False
                    #return True
                
                elif opcode == 0: #No Op
                    print("NoOp")
                    self.counter +=1
                else:
                    raise SyntaxError("Invalid Operation")
            # return False

def main():
    v = UVSim()
    v.program = ["1000","3300","2101","1101","4300"]
    v.run()
    


    # if os.path.getsize("input.txt") > 0:            # If Input file changes or in other words, if input is entered
    #     print("Greater than Zero")
    # else:
    #     print("Less than zero")



    # with open("input.txt","w") as f:
    #     f.write("GRRR")

    # if os.path.getsize("input.txt") > 0:            # If Input file changes or in other words, if input is entered
    #     print("Greater than Zero")
    #     print(os.path.getsize("input.txt"))
    # else:
    #     print("Less than zero")

    
    # with open("input.txt","w") as f:
    #     f.write("1")

    # if os.path.getsize("input.txt") > 0:            # If Input file changes or in other words, if input is entered
    #     print("Greater than Zero")
    #     print(os.path.getsize("input.txt"))
    # else:
    #     print("Less than zero")

    # with open("input.txt","w") as f:
    #     pass

    # if os.path.getsize("input.txt") > 0:            # If Input file changes or in other words, if input is entered
    #     print("Greater than Zero")
    #     print(os.path.getsize("input.txt"))
    # else:
    #     print("Less than zero")
    
if __name__ == "__main__":
    main()
