from uvsim import UVSim
from tkinter import *
from tkinter.simpledialog import askstring

class GUI:              # Eder Sandoval
    def __init__(self):
        self.root = Tk()
        self.simulator = UVSim()
        self.console = None # This gets updated later in the code

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
        stop_button = Button(my_frame, text="Stop",command=self.stop, width=8, height=2, bg="white")

        run_button.grid(row=3, column=0)
        stop_button.grid(row=3, column = 1)
        

        # Create the Console Row 4 and 5
        console_label = Label(my_frame, text="Console", bg="white", fg="black")
        console_label.grid(row=4, column=0, sticky="ew")

        text_scroll = Scrollbar(my_frame)
        text_scroll.grid(row=5, column=4, sticky="ns")

        self.console = Text(my_frame, height=15, width=35, background="lightgray",bd=1, relief="solid", highlightbackground="black",
                             highlightcolor="black", highlightthickness=1,fg="black",yscrollcommand=text_scroll.set, wrap="word",state="disabled") # state="disabled"

        self.console.grid(row=5, column=0, columnspan=4)
        self.read_file()
        self._update_labels(accumulator, counter)

    def _update_labels(self, a, c):
        a.config(text=f"Accumulator: \n{self.simulator.get_accumulator()}")
        c.config(text=f"Counter: \n{self.simulator.get_counter()}")
        self.root.after(1000, self._update_labels, a, c)
        
    def read_file(self, prev=0):
        with open("output.txt","r") as file_in:
            file_in.seek(prev)
            new_content = file_in.read()
            if new_content:
                if new_content[-1] == '|':  # HANDLES INPUT
                    self.console.config(state="normal")
                    self.console.insert(END, new_content[:-1])  # Display prompt
                    #self.console.see(END)  # Scroll to the end to make sure the prompt is visible
                    #self.console.config(state="disabled")

                    # Wait for user input
                    input_data = askstring("Input", new_content[:-1])
                    self.console.insert(END, f" {input_data}")

                    # Process input as needed


                else:   # HANDLES OUTPUT
                    self.console.config(state="normal")
                    self.console.insert(END, new_content)
                    self.console.config(state="disabled")
            new_last_position = file_in.tell()
            self.root.after(1000,self.read_file, new_last_position)


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
    #gui.simulator.program = ["1000", "1100", "1001","1101","2000","3001","2102", "1102" ,"4300"]   # Valid Input
    gui.create_main_window()
    #gui._create_program_display()


if __name__ == "__main__":
    main()