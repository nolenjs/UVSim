from uvsim import UVSim
from tkinter import *

class GUI:              # Eder Sandoval
    def __init__(self):
        self.root = Tk()
        self.simulator = UVSim()

    def stop(self):
        #Function that stops the program (this will probably be placed in the 
        # UVSim class but here as a placeholder so the button doesn't run an error)
        self.simulator._halt()
        pass

    def load(self):
        #Same as stop
        pass

    def save(self):
        # same as stop
        pass

    def _text_editor(self):     # Left side of the screen
        # Create Main Frame
        my_frame = Frame(self.root, background="white")
        my_frame.grid(row=1, column=1, columnspan=2)

        basic_ml_label = Label(my_frame, text="BasicML Program", fg="black", bg="white")
        basic_ml_label.grid(row=0, column=0, columnspan=4, sticky="ew")


        # Create Scrollbar
        text_scroll = Scrollbar(my_frame)
        text_scroll.grid(row=1, column=3, sticky="ns")


        # Create Text Box
        text = Text(my_frame, width=40, height = 20, font=("Arial",16), selectbackground="gray", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, bg="lightgray", fg="black",insertbackground="black")
        text.grid(row=1, column=0, columnspan=3)

        # Configure Scrollbar
        text_scroll.configure(command=text.yview)

        # Create Buttons
        load_button = Button(my_frame, text="Load From File", command=self.load, width=8, height = 2, bg="white")
        save_button = Button(my_frame, text="Save To File",command=self.save, width=8, height=2, bg="white")
    
        load_button.grid(row=4, column = 0)
        save_button.grid(row=4, column = 2)

        # Create Empty Label for Space
        empty_label = Label(my_frame, text="\n", bg="white")
        empty_label.grid(row=3, column=0, columnspan=4, sticky="ew")
        
        

    def _create_program_display(self):  # Right side of the screen
        # Function that dispalys the accumulator, counter, run and stop buttons, and console
        # frame = Frame(self.root)
        my_frame = Frame(self.root, background = "white")
        my_frame.grid(row =1, column=4, columnspan=2)
        
        # Create UVSim label    Row 0
        uvsim_label = Label(my_frame, text="UVSim", fg="black", bg="white", height=3)
        uvsim_label.grid(row=0, column=0, columnspan=4, sticky="ew")

        # Create Accumulator and Counter Displays Row 1 and 2
        accumulator = Label(my_frame, text = f"Accumulator: \n{self.simulator.get_accumulator()}", bg="lightgray", fg="black", width=12, height=2,
                            bd=1, relief="solid", highlightbackground="black",highlightcolor="black",highlightthickness=1, anchor="w", justify="left")
        
        counter = Label(my_frame, text=f"Counter: \n{self.simulator.get_counter()}", bg="lightgray", fg="black", width=12, height=2,
                        bd=1, relief="solid", highlightbackground="black",highlightcolor="black",highlightthickness=1, anchor="w", justify="left")

        accumulator.grid(row=1, column=0)
        counter.grid(row=2, column=0)

        # Create Run and Stop Buttons Row 3
        run_button = Button(my_frame, text="Run", command=self.simulator.run, width=8, height = 2, bg="white")
        stop_button = Button(my_frame, text="Stop",command=self.simulator._halt, width=8, height=2, bg="white")

        run_button.grid(row=3, column=0)
        stop_button.grid(row=3, column = 1)
        

        # Create the Console Row 4 and 5
        console_label = Label(my_frame, text="Console", bg="white", fg="black")
        console_label.grid(row=4, column=0, sticky="ew")

        console = Label(my_frame, height=15, width=35, state=DISABLED, background="lightgray",bd=1, relief="solid", highlightbackground="black",highlightcolor="black",highlightthickness=1)
        console.grid(row=5, column=0, columnspan=4)


    def create_main_window(self):
        self.root.title("UVSim")
        self.root.configure(bg="white")     # changes background color to white
        self.root.configure(bd=3, relief="solid", highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.root.geometry("850x550")   # dimensions of starting gui
        uvsim_label = Label(self.root, text="UVSim",bg="white", fg="black") # Place UVSim label outside frames in corner
        uvsim_label.grid(row=0, column=0, sticky="ew")
        empty_label = Label(self.root, text="                ")


        self._text_editor() # This takes up column 1 and 2
        empty_label.grid(row=0, column=3)   # This takes up column 3
        self._create_program_display() # This takes up column 4 and 5

        self.root.mainloop()
    
def main():
    gui = GUI()
    gui.create_main_window()

if __name__ == "__main__":
    main()