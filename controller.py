from gui import GUI
from uvsim import UVSim
from tkinter.simpledialog import askstring


'''
Controller Class (Controller) contains the interactions between the View (GUI class) and Model (UVSim class). 
The controller class contains a GUI and UVSim object. These objects interact with each other 
throughout the 'run' method, however they are not dependent on each other. 
'''
class Controller():
    def __init__(self):
        self.model = UVSim()          # UVSIM object
        self.view = GUI()            # GUI object

    def get_run(self):
        return self.run_program
    

    '''
    This function is almost exactly the same as the run method in UVSim. The only different is that this method 
    receives the text into the program to run (first line of function). 
    '''    
    def run_program(self):
        self.model.program = self.view.receive_text(self.view.text)     # This gets the text from the text editor and stores it into our program
        self.model.counter = 0          # Reset Counter
        self.model.accumulator = 0      # Reset Accumulator
        self.model.run_program = True   # Make sure run program is True (neccesary for multiple runs)
        while self.model.run_program:
                #Get Next Line
            try:
                current = self.model.program[self.model.counter] #Start at current PC position
                # Validates the Input
                #If that line is empty
                if len(current) == 0:
                    while len(current) == 0:
                        self.model.counter += 1
                        current = self.model.program[self.model.counter]
                        
                if len(current) == 5 and current[0] == '-':
                    if current[1:].isdigit():
                        pass

                elif len(current) == 4:
                    if current.isdigit():
                        pass
                else: 
                    raise SyntaxError("Invalid Operation") 

                #Exract opcode
                if current[0] == "-":
                    self.model.counter += 1
                    # opcode = int(str(current)[:3]) #Get first three digits
                    # IF VARIABLES AREN"T SUPPOSED TO RUN THEN JUST PUT A 
                    
                else:
                    opcode = int(str(current)[:2]) #Get first two digits
                    operand= int(current) % 100 #GeT Last Two Digits
                    print(f"OpCode: {opcode} Operand: {operand}")

                    #Run Operation
                    if opcode == 10:
                        inp = askstring("Input", "Enter valid word:") 
                        word = self.model._read(inp, operand) #READ
                        self.view.append_console(word)

                        
                    elif opcode == 11:
                        word = self.model._write(operand) #WRITE
                        self.view.append_console(word)

                    elif opcode == 20:
                        self.model._load(operand) #LOAD
                    elif opcode == 21:
                        self.model._store(operand) #STORE

                    elif opcode >= 30 and opcode <= 33:
                        self.model._arithmetic(opcode, operand) #ADD

                    elif opcode >= 40 and opcode <= 42:
                        self.model._branch(opcode, operand) #BRANCH
                        self.model.counter += 1

                    elif opcode == 43:
                        #HALT
                        text = self.model._halt()
                        self.view.append_console(text)
                        #return True
                    
                    elif opcode == 0: #No Op
                        print("NoOp")
                        self.model.counter +=1
                    else:
                        print(opcode, )
                        raise SyntaxError("Invalid Operation")
                    self.view._update_labels(self.view.labels[0], self.view.labels[1], self.model.get_accumulator(), self.model.get_counter())

            # return False
            except (SyntaxError, ValueError, IndexError) as e:
                # self.view.console.config(state="normal")
                # self.view.console.insert(END, f"{e}\n")
                # self.view.console.config(state="disabled")
                self.view.append_console(e)
                self.model.run_program = False