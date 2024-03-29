import os
from tkinter import *
from tkinter.simpledialog import askstring
from gui import GUI
'''
UVSim class (Model) contains the logic and manages the application's data. 
It processes data, makes computations, and updates its state accordingly.
'''
class UVSim:
    def __init__(self, counter = 0, accumulator = 0):
        self.counter = counter
        self.accumulator = accumulator
        self.program = []
        self.run_program = True
        self.pause = False


    #Other functions to come, but something to get started
        #kicks and giggles        
                
    def get_accumulator(self):
        return self.accumulator
    
    def get_run(self):
        return self.run
    
    def get_halt(self):
        return self._halt

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
        # print(f"Read From Keyboard to: {location}") #Shout for Testing
        self._check_location(location)
        word = askstring("Input", "Enter valid word:") 
   
        if len(word) == 5 and word[0] == '-':
            if word[1:].isdigit():
                pass

        elif len(word) == 4:
            if word.isdigit():
                pass
        else: 
            raise ValueError("Invalid Input")  
    
        self.program[location] = str(word) #Store word at location in file
        # self.gui.console.config(state="normal")
        # self.gui.console.insert(END, f"Enter valid word: {word}\n")
        # self.gui.console.config(state="disabled")
        self.counter += 1
        return word

        
    
    def _write(self, location): #11
        '''Writes a Word from a specific Memory Location to the screen.'''
        # print(f"Print From {location} to Screen") #Shout for Testing
        self._check_location(location)
        word = self.program[location] #Get word from location in file
        print(word)
        # self.gui.console.config(state="normal")
        # self.gui.console.insert(END, f"{word}\n")
        # self.gui.console.config(state="disabled")
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

    def _halt(self):
        '''Pauses the Program'''
        print(f"Halt the Program") #Shout for Testing
        self.run_program = False
        #End program Handled By run Method

