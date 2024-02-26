from uvsim import UVSim
from tkinter import *

class GUI:              # Eder Sandoval
    def __init__(self):
        self.root = Tk()
        self.simulator = UVSim()

    def stop(self):
        #Function that stops the program (this will probably be placed in the 
        # UVSim class but here as a placeholder so the button doesn't run an error)
        pass

    def load(self):
        #Same as stop
        pass

    def save(self):
        # same as stop
        pass

    

    def _text_editor(self):
        # Create Main Frame
        # my_frame = Frame(self.root)
        my_frame = LabelFrame(self.root, text="text editor frame")
        my_frame.grid(row=2, column=1, columnspan=2)

        # Create Scrollbar
        text_scroll = Scrollbar(my_frame)
        text_scroll.grid(row=2, column=2, sticky="ns")


        # Create Text Box
        text = Text(my_frame, width=40, height = 20, font=("Arial",16), selectbackground="gray", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, bg="lightgray", fg="black",insertbackground="black")
        text.grid(row=2, column=1)

        # Configure Scrollbar
        text_scroll.configure(command=text.yview)

        # Create Menu
        # my_menu = Menu(self.root)
        # self.root.config(menu=my_menu)

        # # Add File Menu
        # file_menu = Menu(my_menu)
        # my_menu.add_cascade(label="File", menu=file_menu)
        # file_menu.add_command(label="Open")
        # file_menu.add_command(label="Save")

    def _create_program_display(self):
        # Function that dispalys the accumulator and the counter
        # frame = Frame(self.root)
        frame = LabelFrame(self.root, text="Simulator")
        frame.grid(row=2, column = 4, columnspan = 2)


        accumulator = Label(frame, text = f"Accumulator: {self.simulator.get_accumulator()}", bg="lightgray", fg="black", width=30, height=4)
        accumulator.config(highlightbackground="black", highlightcolor="black", highlightthickness=1)
        accumulator.pack()

        # counter = Label(frame, text=self.simulator.get_counter(), bg="white")

    def _create_labels(self):
        # Function that creates the labels. Each label needs to be created, then added to main window
        uvsim_label = Label(self.root, text="UVSim",bg="white", fg="black") # fg text color, bg background color
        
        basic_ml_label = Label(self.root, text="BasicML Program", fg="black", bg="white")
        
        uvsim_label_big = Label(self.root, text="UVSim", fg="black",bg="white")
        uvsim_label_big.config(font=("Arial",16))  

        # Empty label to create a gap between the text editor and UVSim side
        empty_label = Label(self.root,text="GRRRRRRRR",bg="white", fg="white") 


        # Add labels to main grid
        uvsim_label.grid(row=0,column=0)        # add to grid window
        basic_ml_label.grid(row=1, column=1)    # add to grid window
        uvsim_label_big.grid(row=1, column = 5) # add to grid window
        empty_label.grid(row=0, column=4)


    def _create_buttons(self):
        # Funciton that creates the buttons. Each button needs to be created, then added to main window
        run_button = Button(self.root, text="Run", command=self.simulator.run)
        # when running without a program argument, our program throws an error, change run function so that it doesn't run without if len(program) == 0: return
        stop_button = Button(self.root, text="Stop", command=self.stop)    # add a method in uvsim that stops quits the program
        
        load_button = Button(self.root, text="Load From File", command=self.load)
        save_button = Button(self.root, text="Save To File",command=self.save)



        run_button.grid(row=3,column=5)
        stop_button.grid(row=3,column=6)

        # These buttons might need to be in the text editor function
        load_button.grid(row=4, column = 1)
        save_button.grid(row=4, column = 2)


    def _draw_lines(self):
        # Function that draws out the lines to make our GUI pretty :)
        pass



    def create_main_window(self):
        self.root.title("UVSim")
        self.root.configure(bg="white")     # changes background color to white
        self.root.geometry("800x500")   # dimensions of starting gui
        

        self._text_editor()
        self._create_labels()
        self._create_buttons()
        self._create_program_display()

        self.root.mainloop()
    
def main():
    gui = GUI()
    gui.create_main_window()

if __name__ == "__main__":
    main()